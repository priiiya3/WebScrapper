import requests
from bs4 import BeautifulSoup

def scrape_text_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        extracted_text = soup.get_text()
        
        # Remove extra spaces, newlines, and unknown characters
        cleaned_text = ' '.join(extracted_text.split())
        
        return cleaned_text
    else:
        return None
