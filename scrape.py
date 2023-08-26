#import necessary library
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

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
    
  
  
# Load the CSV file
csv_filename = "./scraped_article.csv"
data = pd.read_csv(csv_filename)
  
# Extract the 'content' column
content_column = data['content']

# Create a list to store sentences
sentences_list = []

# Iterate through the content column and split into sentences
for content in content_column:
    sentences = content.split('.')  # Split by full stop
    sentences = [s.strip() for s in sentences if s.strip()]  # Remove empty sentences
    sentences_list.extend(sentences)

# Create a new DataFrame from the sentences list
sentences_df = pd.DataFrame({'Sentences': sentences_list})

# Save DataFrame to CSV
sentences_df.to_csv('sentences.csv', index=False)
    
    
