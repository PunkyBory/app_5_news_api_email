import requests
from send_email import send_email

API_KEY = "d3277419472b45b198e60e8595055c9c"
url = "https://newsapi.org/v2/everything?q=tesla&from=2026-10" \
      "-25&sortBy=publishedAt&apiKey=d3277419472b45b198e60e8595055c9c"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the articles title and decription
body = " "
for article in content["articles"]:

    title = article.get("title") or ""
    description = article.get("description") or ""

    body = body + title + "\n" + description + 2*"\n"

body = body.encode("utf-8")
send_email(body)


