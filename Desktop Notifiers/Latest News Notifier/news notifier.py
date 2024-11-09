from plyer import notification 
import requests
import json
import time

def notify_news(title1, description, source):

    notification.notify(
        title=title1,
        message=description,
        timeout=10,
        app_name=source
    )

def fetch_news():

    # API key
    api_key = 'd656c31a50bf44a1a12101c427f7a871'

    # API endpoint
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'

    # Make the GET request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        news_data = response.json()
        
        # Extract and print desired information
        articles = news_data['articles']
        
        for article in articles:

            source_name = article['source']['name']
            source = f"{source_name}"
            title = article['title']
            title1 = f"{title}"
            description = article['description']
            description1 = f"{description}"
            

            notify_news(title1, description1, source)
            time.sleep(60.0)
            

    else:
        print(f"Failed to get the news data. Status code: {response.status_code}")

fetch_news()
