# Web Scraping App using Django

This is a simple web application built with Django that allows users to input a URL, scrape text from a webpage, and save the extracted text to a file. The project includes a basic front-end interface using HTML and Bootstrap for styling.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python (version 3.8 or higher)
- Django (version 4.1.4 or compatible)
- Requests (for making HTTP requests)
- BeautifulSoup (for web scraping)
- Bootstrap (for styling the front-end)

### Installation

1. Clone the repository:
git clone https://github.com/your-username/web-scraping-app.git

2. Change to the project directory:
cd web-scraping-app

3. Install the required dependencies:
pip install -r requirements.txt

4. Start the Django development server:
python manage.py runserver



## Usage

1. Access the web application by navigating to `http://127.0.0.1:8000/` in your web browser.
2. Enter a URL in the input box and click the "Submit" button to scrape text from the webpage.
3. If the scraping is successful, the extracted text will be saved to a unique text file inside the folder named 'scraped_data'.
4. A success message and the URL/name of the extracted text file will appear.

## Features

- Input a URL to scrape text from a webpage.
- Display an alert message on successful text extraction.
- Save each scraped file with a different name to avoid overwriting.




