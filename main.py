import requests
import os
from send_email import configure, send_email

configure()

category = "tesla"
api_key = os.getenv('API_KEY')
url = "https://newsapi.org/v2/everything?" \
       f"q={category}&sortBy=publishedAt&" \
       f"apiKey={api_key}" \
       "&language=en"

request = requests.get(url)
content = request.json()

txt = "Subject: News Digest"
for article in content['articles'][:20]:
    if article['title'] is not None and article['description'] is not None:
        txt = txt + '\n' + article['title'] + '\n' + article['description'] + '\n' + article['url'] + 2 * '\n'

txt = txt.encode()

send_email(txt)
