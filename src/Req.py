import requests

user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"

def get(endpoint):
    response = requests.get(endpoint, headers = { "USER-AGENT": user_agent })
    response.raise_for_status()

    return response.json()
