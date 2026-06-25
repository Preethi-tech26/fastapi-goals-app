# Session 3 - June 15 2026
# Learned: requests library, calling REST APIs, parsing JSON

import requests

response = requests.get("https://api.github.com")

data = response.json()
print(type(data)) #shows it's a dictionary
print(data["current_user_url"])
print(data["repository_url"])

print(response.status_code)
#print(response.text)clear'