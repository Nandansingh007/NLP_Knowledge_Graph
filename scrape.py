#import necessary library
import requests
from bs4 import BeautifulSoup
import csv

# URL of the article to scrap the data
article_url = "https://english.onlinekhabar.com/prakriti-where-the-gods-reside.html"

# Send GET request to URL
response = requests.get(article_url)

if response.status_code == 200:
    
    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the article title
    
    # The artice title, date and content class is different for different website, inspect it and find it
    title_container = soup.find('div', class_='ok-post-header')
    article_title = title_container.find('h1').get_text().strip()
    
    # Find the article date
    article_date = soup.find('span', class_='ok-post-date').get_text().strip()
    
    # Find the article content
    article_content = soup.find('div', class_='ok-details-content-left')
    
    if article_content:
        
        # Extract paragraphs from the article
        paragraphs = article_content.find_all('p')
        
        # Extract and save the extracted data to a CSV file
        csv_filename = "scraped_article.csv"
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["title", "date", "content"])
            
            content = ""
            for paragraph in paragraphs:
                content += paragraph.get_text().strip() + " "
            
            csv_writer.writerow([article_title, article_date, content])
        
        print(f"Article data saved to {csv_filename}")
    else:
        print("Article content not found on the page.")
                   
else:
    print("Failed to fetch the article.")
    
    
