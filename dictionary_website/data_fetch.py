import requests

url = "https://owlbot.info/api/v4/dictionary"
headers = {
    "Authorization": "Token 876ab2e955ae814a5cf97ed6c47c15d4e5108cbc"
}


def search_word(word):
    res = requests.get(url=f"{url}/{word}", headers=headers)
    data = res.json()
    return data.get('definitions')
