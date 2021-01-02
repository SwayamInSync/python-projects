import requests
from datetime import datetime


APP_ID = "959e9ea0"
API_KEY = "a8aa62d90467ca872b91fa4593276b3c"
nutrionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

sheety_endpoint = "https://api.sheety.co/bdbc231c7faf14c1881bf01027bd7abc/workoutsTracking/workouts"



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

    response = requests.post(url=sheety_endpoint, json=body, auth=("rootacess3000", "rootacess"))
    print(response.text)