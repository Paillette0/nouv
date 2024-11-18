

import requests
from bs4 import BeautifulSoup

# URL cible
url = "http://quotes.toscrape.com/"

# Envoyer une requête GET pour récupérer le contenu HTML
response = requests.get(url)

# Vérifier le statut de la requête
if response.status_code == 200:
    # Analyser le contenu avec BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Trouver toutes les citations (divs avec la classe 'quote')
    quotes = soup.find_all('div', class_='quote')

    # Parcourir les citations et extraire les informations
    for quote in quotes:
        # Citation
        text = quote.find('span', class_='text').text.strip()

        # Auteur
        author = quote.find('small', class_='author').text.strip()

        # Tags
        tags = [tag.text for tag in quote.find_all('a', class_='tag')]

        # Afficher les informations
        print(f"Citation : {text}")
        print(f"Auteur : {author}")
        print(f"Tags : {', '.join(tags)}\n")
else:
    print(f"Erreur : Impossible d'accéder au site (code {response.status_code}).")
