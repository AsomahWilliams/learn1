import requests
from bs4 import BeautifulSoup

def fetch_news_headlines(url):
    try:
        # Send a GET request to the news website
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the headlines (this will depend on the website's structure)
        # Example for a common news site (you may need to adjust the selector)
        headlines = soup.find_all('h2', class_='headline', limit=5)  # Adjust the tag and class as needed

        # Extract and print the text of the headlines
        for i, headline in enumerate(headlines, start=1):
            print(f"{i}. {headline.get_text(strip=True)}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# URL of the news website (example: CNN, BBC, etc.)
news_url = 'https://www.bbc.com/news'  # Change this to the desired news site

# Fetch and display the news headlines
fetch_news_headlines(news_url)