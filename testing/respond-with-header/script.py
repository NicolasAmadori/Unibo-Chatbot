import os
import requests

def scarica_file(url, nome_file, headers=None):
    try:
        risposta = requests.get(url, headers=headers)

        if risposta.status_code == 200:
            script_directory = os.path.dirname(os.path.abspath(__file__))
            percorso_file = os.path.join(script_directory, nome_file)

            with open(percorso_file, 'wb') as file:
                file.write(risposta.content)
            print(f"File \"{nome_file}\" scaricato con successo.")
        else:
            print(f"Errore durante il download del file. Codice di stato: {risposta.status_code}")
    except Exception as e:
        print(f"Si è verificato un errore durante il download del file: {e}")

prefix = "https://r.jina.ai/"
url = "https://www.unibo.it/it/ateneo/organizzazione-e-sedi/servizi-di-ateneo/servizi-online/servizi-online-per-studenti/guida-servizi-online-studenti/liste-di-distribuzione-docenti-studenti"

#Testing returing values for every value of the jina header "x-respond-with"
#header value -> file type
types = {
    "markdown": "txt",
    "html": "txt",
    "text": "txt",
    "screenshot": "png"
}

scarica_file(prefix + url, "no_header.txt") #Requesting page without "x-respond-with" header

#Requesting pages using "x-respond-with" header
for t in types.keys():
    header_personalizzati = {"x-respond-with": t}
    nome_file = f"{t}.{types[t]}"
    scarica_file(prefix + url, nome_file, headers=header_personalizzati)
