import requests
from datetime import *
import os

# ---------------------------------------Nurtionix API----------------------------------------------------------------
APP_ID=os.environ.get("APP_ID")

API_KEY=os.environ.get("API_KEY")

X_REMOTE_USER_ID=os.environ.get("XTHIS_IS_TOKEN")
BEARER_AUTH="Bearer YOUR KEYWORD"
postUrl = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_program = input("what program do you want to record ")
exercise_param = {

    "query": exercise_program,
    "gender": "male",
    "age": 21
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Authorization": BEARER_AUTH
}

response = requests.post(url=postUrl, json=exercise_param, headers=headers)
result = response.json()

# ------------------------------------sheetly API -------------------------------------------

new_sheet_api = "https://api.sheety.co/d0b0e765cae5f17c187e8e18607f0d4b/myWorkouts/workouts"

today_date = datetime.now().strftime("%d:%m:%Y")
today_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_input = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=new_sheet_api, json=sheet_input, headers=headers)
    print(sheet_response.text)
