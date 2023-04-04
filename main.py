import requests
from datetime import datetime

MY_LAT = 12.932892  # Your latitude
MY_LONG = 77.571201  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.
def is_overhead():
    global MY_LAT, MY_LONG, iss_longitude, iss_longitude
    if (MY_LONG - 5.0 < iss_longitude < MY_LONG + 5.0) and (MY_LAT - 5 < iss_latitude < MY_LAT + 5):
        return True
    return False


def is_dark():
    global time_now, sunset, sunrise
    if time_now.hour > sunset or time_now.hour < sunset:
        return True
    return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data2 = response.json()
print(data2)
sunrise = int(data2["results"]["sunrise"].split("T")[1].split(":")[0]) + 5
sunset = int(data2["results"]["sunset"].split("T")[1].split(":")[0]) + 5
print(sunset, sunrise)
time_now = datetime.now()
print(time_now)
# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
