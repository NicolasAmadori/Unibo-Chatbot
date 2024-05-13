import requests

def get_content_length(url):
    try:
        # Effettua la richiesta GET all'URL fornito
        response = requests.get(url)

        # Controlla se l'header Content-Length è presente nella risposta
        if 'Content-Length' in response.headers:
            content_length = response.headers['Content-Length']
            print(f"Content-Length: {content_length}")
        else:
            print("Content-Length non presente nella risposta.")
    except requests.exceptions.RequestException as e:
        print(f"Errore durante la richiesta: {e}")

# URL di esempio
url = 'https://www.unimi.it/it/internazionale'

# Ottieni e stampa l'header Content-Length
get_content_length(url)
