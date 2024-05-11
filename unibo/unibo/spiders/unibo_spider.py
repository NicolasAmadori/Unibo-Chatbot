import scrapy
from ..items import PagesList
from urllib.parse import urljoin

class UniboSpiderSpider(scrapy.Spider):
    name = "unibo_spider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]
    jina_prefix = "https://r.jina.ai/"

    def __init__(self, *args, **kwargs):
        super(UniboSpiderSpider, self).__init__(*args, **kwargs)
        self.visited_urls = set()
        self.all_links = []
        self.isFirst = True

    def parse(self, response):
        # copy = self.isFirst
        # if(self.isFirst):
        #     self.isFirst = False
        urls = response.css('a::attr(href)').getall()
        # filtered_urls = list(filter(lambda url: (not url.startswith("#")), urls)) #Remove link starting with #
        # mapped_urls = list(map(lambda url: (url if url.startswith("http") else urljoin(response.url, url)), filtered_urls)) #Mapping relative urls to absolute urls
        # unseen_urls = list(filter(lambda url: (url not in self.visited_urls), mapped_urls))
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse_link(self, response):
        # Trova tutti i link nella pagina e li stampa
        links = response.css('a::attr(href)').getall()
        for link in links:
            yield {
                'url': response.urljoin(link)
            }
            # Visita ogni link trovato
            yield scrapy.Request(response.urljoin(link), callback=self.parse_link)