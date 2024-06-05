from bs4 import BeautifulSoup
import requests

import requests
from bs4 import BeautifulSoup

def scrape_quotes(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all quote elements on the page
        quotes = soup.find_all('div', class_='quote')

        # Extract and print quotes and their authors
        for quote in quotes:
            text = quote.find('span', class_='text').get_text()
            author = quote.find('small', class_='author').get_text()
            print(f'"{text}" - {author}')
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

if __name__ == "__main__":
    url = 'http://quotes.toscrape.com/'
    scrape_quotes(url)