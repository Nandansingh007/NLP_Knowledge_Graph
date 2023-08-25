#import necessary library
import requests
from bs4 import BeautifulSoup

# URL of the article to scrap the data
article_url = "https://english.onlinekhabar.com/gold-smuggling-case-commission.html"

# Send GET request to URL
response = requests.get(article_url)

if response.status_code == 200:
    
    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the article content
    article_content = soup.find('div', class_='site')
    
    # Extract paragraphs from the article
    paragraphs = article_content.find_all('p')
    
    # Extract and print the text from each paragraph
    for paragraph in paragraphs:
        print(paragraph.get_text())
        
else:
    print("Failed to fetch the article.")
