import requests
from datetime import datetime
API_ID = "86e6a8cd"
API_KEY = "d419f13de624c922fdc7b4a0628bbf80	"
GENDER = "female"
HEIGHT = 167
AGE = 23
WEIGHT = 62.5
Token = "Bearer myfavouriteworkoutroutines"
# env variables

today = datetime.now()
today_string = today.strftime("%Y/%m/%d")
time = today.strftime("%I%M")
exercise_text = input(f"what did you do for today's exercise?")
headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}
# print(headers)
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
workout = {
    "query": exercise_text,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
    "gender": GENDER,
}
response = requests.post(url=exercise_endpoint, json=workout, headers=headers)
result = response.json()
# sheety_endpoint = "https://api.sheety.co/2c7e0fbb73b0d0293e1945cf35b19c26/workoutTracking/workouts"
# response = requests.get(url=sheety_endpoint)
# print(response.text)

sheety_post_endpoint = "https://api.sheety.co/2c7e0fbb73b0d0293e1945cf35b19c26/workoutTracking/workouts"
# authorization
auth_header = {
    "Authorization": Token
}
for exercise in result["exercises"]:
    my_data = {
        "workout": {
            "date": today_string,
            "Time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    # print(my_data)
    sheety_response = requests.post(sheety_post_endpoint, json=my_data, headers=auth_header)
    # print(sheety_response.text)
