import requests
from twilio.rest import Client

url = "https://api.openweathermap.org/data/2.5/onecall"
owm_api = "<your open weather map API_KEY>"

account_sid = "<your twilio account_sid>"
auth_token = "<your twilio auth_token>"

parameters = {
    "lat": 30.5928,
    "lon": 114.3055 ,
    "units": "metric",
    "appid": owm_api,
    "exclude": "current,minutely,daily,alerts"
}

is_rain = False

response = requests.get(url=url, params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly_data = weather_data["hourly"]
for n in range(0, 12):
    if int(hourly_data[n]["weather"][0]["id"]) < 700:
        is_rain = True
        break

if is_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Swayam today clouds will rain anytime, so take umbrella with you",
        from_='<number given by twilio>',
        to='<your verified phone number>'
    )
    print(message.status) # queued status means msg is sent
else:
    pass
