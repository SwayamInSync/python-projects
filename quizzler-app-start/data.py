import requests
parameters = { # always make your parameters in json format
    "amount": 10,
    "type": "boolean",
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
question_data = response.json()["results"]
