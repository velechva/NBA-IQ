import requests

def get(endpoint):
    response = requests.get(endpoint, headers = { "USER-AGENT": user_agent })
    response.raise_for_status()

    return response.json()
