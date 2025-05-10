import requests
import time
from twilio.rest import Client
from config import NEWSDATA_API_KEY, TOPIC, FROM_WHATSAPP_NUMBER, TO_WHATSAPP_NUMBER, ACCOUNT_SID, AUTH_TOKEN

# Initialize Twilio Client
client = Client(ACCOUNT_SID, AUTH_TOKEN)

def get_latest_news():
    # Construct the News API URL
    url = (
        f"https://newsapi.org/v2/everything?"
        f"apikey={NEWSDATA_API_KEY}&"
        f"q={TOPIC}&"  # Search query (can be changed to any topic)
        f"sortBy=publishedAt&"
        f"language=en&page=1"  # Specify language and number of results per page
    )

    # Make the GET request to NewsAPI
    response = requests.get(url)
    data = response.json()  # Parse the response as JSON

    # Check if the request was successful and has articles
    if data["status"] == "ok" and data["totalResults"] > 0:
        messages = []
        for article in data["articles"]:
            title = article["title"]
            source = article["source"]["name"]
            published = article["publishedAt"]
            url = article["url"]
            messages.append(f"🗞️ *{title}*\n📍{source} | 🕒 {published}\n🔗 {url}")
        
        # Return formatted messages
        return "\n\n".join(messages)
    else:
        return "⚠️ No news found."

def send_whatsapp_message(message):
    # Send the news message to your WhatsApp number using Twilio API
    client.messages.create(
        from_=FROM_WHATSAPP_NUMBER,  # Twilio sandbox number
        body=message,  # Message content
        to=TO_WHATSAPP_NUMBER  # Your phone number
    )

while True:
    # Get the latest news
    news = get_latest_news()

    # Send the news via WhatsApp
    send_whatsapp_message(news)

    # Wait for 1 hour (3600 seconds) before fetching the news again
    time.sleep(3600)
