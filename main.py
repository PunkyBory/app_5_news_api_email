import os
import requests
from send_email import send_email
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
print(f"Geladen API Key:{api_key}")

url = "https://newsapi.org/v2/everything?" \
      "q=tesla" \
      "&from=2026-10-25" \
      "&sortBy=publishedAt&" \
      f"apiKey={api_key}"\
      "&language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

print(content)

# Access the articles title and description
body = " "
for article in content["articles"]:

    title = article.get("title") or ""
    description = article.get("description") or ""

    body = body + title + "\n" + description + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(body)


