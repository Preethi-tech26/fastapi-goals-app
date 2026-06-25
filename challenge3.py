import requests

def call_public_api():
 response = requests.get("https://api.github.com/users/octocat")
 data = response.json()
 print(data["name"])
 print(data["public_repos"])
 print(data["followers"])


call_public_api()