import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import os
from urllib.parse import urlparse

class UniboCrawlerSpider(CrawlSpider):
    name = "unibo_crawler"
    jina_prefix = "https://r.jina.ai/"

    # allowed_domains = ["unibo.it", "r.jina.ai"]
    # start_urls = ["https://www.unibo.it/en"]

    allowed_domains = ["corsi.unibo.it", "r.jina.ai"]
    start_urls = ["https://corsi.unibo.it/laurea/IngegneriaScienzeInformatiche/index.html"]
    printOnlyUrl = True

    def __init__(self, *args, **kwargs):
        super(UniboCrawlerSpider, self).__init__(*args, **kwargs)
        self.i = 0

    general_link = Rule(LinkExtractor(restrict_css="a"), callback="download_jina", follow=True)

    rules = (
        general_link,
    )

    def stampa_url(self, response):
        full_link = self.jina_prefix + response.url
        self.i+=1
        yield {
            'id': self.i,
            'url': full_link
        }

    def download_jina(self, response):
        full_link = self.jina_prefix + response.url
        headers = {
            "x-respond-with":"markdown"
        }
        yield scrapy.Request(full_link, callback=self.parse_item_from_request, headers=headers, errback=self.handle_error)

    def parse_item_from_request(self, response):
        self.i+=1
        original_url = response.url.replace("https://r.jina.ai/", "")
        if self.printOnlyUrl:
            filename = "links.txt"
            path = os.path.join("pagine", filename) #Concateno il percorso

            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "a", encoding="utf-8") as f:
                f.write(original_url + "\n")
                
            yield {
                'id': self.i,
                "link": original_url
            }
        else:
            filename = str(self.i) + ".txt"

            
            url = urlparse(original_url)
            path_segments = [segment[:50] for segment in url.path.split('/')] #Limito a 50 caratteri i nomi delle directory
            path = os.path.join("pagine", *path_segments, filename) #Concateno il percorso

            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(original_url + "\n\n")#Lascio traccia del link della pagina scaricata
                f.write(response.text)
            
            yield {
                'id': self.i
            }

    def handle_error(self, failure):
        self.logger.error(repr(failure))