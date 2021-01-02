import requests
from datetime import datetime


APP_ID = <Your nutritionix app_id>
API_KEY = <your nutritionix api_key>
nutrionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

sheety_endpoint = <your sheety endpoint>



headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

workout_data = {
    "query": input("Tell me which exercise you did: "),
    "gender": "male",
    "weight_kg": 80,
    "height_cm": 182.5,
    "age": 19,
}



res = requests.post(url=nutrionix_endpoint, json=workout_data, headers=headers)
result = res.json()

for exercise in result["exercises"]:
    body = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response = requests.post(url=sheety_endpoint, json=body, auth=(<sheety username>, <sheety password>))
    print(response.text)
