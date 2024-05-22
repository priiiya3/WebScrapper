import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.shortcuts import render
from .forms import URLForm

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

def home(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            extracted_data = scrape_text_from_url(url)

            if extracted_data:
                # Return the extracted data as a downloadable file response
                response = HttpResponse(extracted_data, content_type='text/plain')
                response['Content-Disposition'] = 'attachment; filename="extracted_text.txt"'
                return response
            else:
                message = 'Error: Unable to extract text.'
                return render(request, 'scraper/home.html', {'form': form, 'message': message})
    else:
        form = URLForm()
    return render(request, 'scraper/home.html', {'form': form})
