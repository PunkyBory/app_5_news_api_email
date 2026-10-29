import requests

API_KEY = "d3277419472b45b198e60e8595055c9c"
url = "https://newsapi.org/v2/everything?q=tesla&from=2026-09-" \
      "29&sortBy=publishedAt&apiKey=d3277419472b45b198e60e8595055c9c"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the articles title and decription
for article in content["articles"]:
      print(article["title"])
      print(article["description"])


