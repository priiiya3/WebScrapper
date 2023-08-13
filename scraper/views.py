import os
from django.shortcuts import render
from .forms import URLForm
from .scrape import scrape_text_from_url

def home(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            extracted_data = scrape_text_from_url(url)

            if extracted_data:
                # Generate a unique filename based on a counter
                counter = 1
                while os.path.exists(f'extracted_text_{counter}.txt'):
                    counter += 1
                filename = f'extracted_text_{counter}.txt'

                # Write extracted data to the unique file
                with open(filename, 'w', encoding='utf-8') as file:
                    file.write(extracted_data)

                message = f'Text extracted and saved successfully as {filename}.'
            else:
                message = 'Error: Unable to extract text.'

            return render(request, 'scraper/home.html', {'form': form, 'message': message})
    else:
        form = URLForm()
    return render(request, 'scraper/home.html', {'form': form})
