#import necessary library
import requests
from bs4 import BeautifulSoup

# URL of the article to scrap the data
article_url = "https://english.onlinekhabar.com/prakriti-where-the-gods-reside.html"

# Send GET request to URL
response = requests.get(article_url)

if response.status_code == 200:
    
    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the article title
    title_container = soup.find('div', class_='ok-post-header')
    article_title = title_container.find('h1').get_text().strip()
    
    # Find the article date
    article_date = soup.find('span', class_='ok-post-date').get_text().strip()
    
    # Find the article content
    article_content = soup.find('div', class_='ok-details-content-left')
    
    # Extract paragraphs from the article
    paragraphs = article_content.find_all('p')
    
    # Print the content of each paragraph after excluding specific lines
    for paragraph in paragraphs:
        paragraph_text = paragraph.get_text().strip()
        
        # Exclude lines that start with "Home »" or "Kathmandu, ..."
        if not paragraph_text.startswith("Home »") and not paragraph_text.startswith("Kathmandu, "):
            print(paragraph_text)
    
               
else:
    print("Failed to fetch the article.")
    
    
