import requests

TOKEN = "XXX"
PAGE_ID = "1021302557732355"

url = f"https://graph.facebook.com/v22.0/{PAGE_ID}?fields=name&access_token={TOKEN}"
r = requests.get(url)
print(f"Status: {r.status_code}")
print(f"Response: {r.text}")
