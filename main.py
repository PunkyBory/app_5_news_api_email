import requests

API_KEY = "d3277419472b45b198e60e8595055c9c"
url = "https://newsapi.org/v2/everything?q=tesla&from=2026-09-" \
      "29&sortBy=publishedAt&apiKey=d3277419472b45b198e60e8595055c9c"

request = requests.get(url)
content = request.text
print(content)