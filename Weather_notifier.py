import requests
from twilio.rest import Client

API_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "YOUR_API_KEY"  # You Have to Keep your own api key,api link:https://openweathermap.org/api/one-call-api

account_sid = 'YOUR_TWILIO_ACCOUNT_ID'  # You have to keep your own account twilio credentials
auth_token = 'YOUR_TWILIO_ACCOUNT_AUTH_TOKEN'

# feel free to change the latitude and longitude below
parameters = {"lat": 17.385044, "lon": 78.486671, "appid": API_KEY, "exclude": "current, minutely, daily, alerts"}
response = requests.get(API_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()
will_rain = False
for i in range(12):
    weather_id = data["hourly"][i]["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today,Don't forget to bring a umbrella.",
        from_='YOUR_TWILIO_ACCOUNT_GENERATED_PHONE_NUMBER',  # you have to keep the new phone number generated in twilio
        to='NUMBER_FOR_WHICH_YOU_WANT_TO_GET_MESSAGE'  # you have to keep the number of which you want to get message
    )

    print(message.sid)
