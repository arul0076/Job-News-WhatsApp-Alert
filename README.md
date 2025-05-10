# WhatsApp News Bot with Python, News APIs & Twilio - Complete Guide

This project allows you to send real-time job-related news updates directly to your WhatsApp using Python, **NewsAPI** for fetching news articles, and **Twilio** for WhatsApp messaging.

---

## 📅 Step-by-Step Setup Guide

### 1. 📲 **Twilio WhatsApp API Setup**
- Go to [Twilio WhatsApp](https://www.twilio.com/whatsapp).
- Sign up or log in to Twilio.
- Navigate to **Messaging > Try it Out > Send a WhatsApp Message**.
- **Activate WhatsApp Sandbox**:
    - You will get a number like `+14155238886`.
    - Send a message like `join <code>` from your WhatsApp to this number (only once per 72 hours).
- **Get your Account SID and Auth Token** from the console.
- **Note down the sandbox number** and your verified WhatsApp number.

### 2. 🌐 **News API Setup (Option 1: NewsAPI.org)**
- Go to [NewsAPI.org](https://newsapi.org).
- Create a free account and get your **API key**.
- Use the following endpoint for fetching news:
    - `https://newsapi.org/v2/everything?q=TOPIC&apiKey=YOUR_KEY`

---

## 🛠️ **Installation**

1. Clone the repository:
    ```bash
    git clone https://github.com/arul0076/Job-News-WhatsApp-Alert.git
    cd whatsapp-job-news-bot
    ```

2. Install required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up **config.py** with your Twilio credentials and NewsAPI key.

    ```python
    # config.py
    TWILIO_ACCOUNT_SID = 'your_account_sid'
    TWILIO_AUTH_TOKEN = 'your_auth_token'
    TWILIO_WHATSAPP_NUMBER = 'whatsapp:+14155238886'
    VERIFIED_WHATSAPP_NUMBER = 'whatsapp:+your_verified_number'
    NEWSAPI_KEY = 'your_newsapi_key'
    ```

4. Run the script:
    ```bash
    python job_news_whatsapp_bot.py
    ```

---

## 📢 **How It Works**
- The script fetches job-related news articles from **NewsAPI**.
- It filters articles related to job openings, recruitment trends, and hiring.
- The filtered news is sent to your WhatsApp number using **Twilio's WhatsApp API**.
- The news updates are sent hourly, ensuring you receive the latest job-related news.

---

## 🤖 **Contributing**

Feel free to fork, open issues, and submit pull requests. Contributions are always welcome!

---

## 📜 **License**
This project is open source and available under the MIT License.
