import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Send request to the site
url = 'https://quotes.toscrape.com'
response = requests.get(url)

# Step 2: Parse the HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Find all quote blocks
quotes_data = []

quotes = soup.find_all('div', class_='quote')
for quote in quotes:
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    tags = [tag.text for tag in quote.find_all('a', class_='tag')]

    quotes_data.append({
        'quote': text,
        'author': author,
        'tags': ', '.join(tags)
    })

# Step 4: Write data to CSV
with open('quotes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['quote', 'author', 'tags']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for quote in quotes_data:
        writer.writerow(quote)

print("✅ Scraped quotes saved to 'quotes.csv'")
