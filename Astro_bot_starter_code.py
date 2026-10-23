#Contains partially completed code with sections for you to complete
#IT IS MANDATORY TO USE THE RESOURCE PROVIDED
#The starter code is structured into functions and modules. You are required to complete the missing sections while maintaining this modular design.  Further step by step instructions can be found in the appendix A of this assignment brief. 
#For extended features implement it within the existing modular structure. The new feature must be triggered using a new command (e.g., /stars, /moon, /sky) and follow the same approach 
#Use Git for version control. Maintain a repository on GitHub to track your project’s progress and changes. Ensure regular commits for each step with meaningful messages that document your step by stepdevelopment process. 

# =========================
# REQUIRED LIBRARIES
# =========================

from asyncio import timeout
from urllib import error, response

import requests #complete the import statement to include the requests library
import json #complete the import statement to include the json library
import time #complete the import statement to include the time library
from datetime import datetime ,timezone#complete the import statement to include the datetime library

# =========================
# CONFIGURATION FUNCTIONS
# =========================#

#ask the user for the Webex token or use a hard-coded token. Return the token in the format "Bearer <token>"
def get_webex_token():
    choice = input("Use hard-coded Webex token? (y/n): ").lower().strip()

    if choice == "n":
        token = input("Enter your Webex Access Token: ").strip()
        return f"Bearer {token}"

    return "Bearer Token"  # Replace TToken with your actual hard-coded token

#ask the user for the Weather API key or use a hard-coded key. Return the key in the format "Bearer <key>"
def get_api_key(prompt, hardcoded_key):
    choice = input(f"Use hard-coded {prompt}? (y/n): ").lower().strip()

    if choice == "n":
        return input(f"Enter your {prompt}: ").strip()

    return "Bearer Api Key"  # Replace Api Key with your actual hard-coded API key


# =========================
# WEBEX FUNCTIONS
# =========================
def get_rooms(token):
    url = "https://webexapis.com/v1/rooms"#URL to fetch rooms from Webex API
    headers = {"Authorization": token}
    try:
        response = requests.get(url, headers=headers,timeout=10)#complete the request to get rooms using requests.get with the url and headers
        if response.status_code != 200:#complete the condition to check if the response status code is not 200:
                print("Error fetching rooms:", response.status_code)
                return []

        return response.json().get("items", [])
    except requests.exceptions.RequestException as error:
        print("Error fetching rooms:", ValueError)
        return []
    


def print_rooms(rooms):
    for room in rooms:
        print(f"Room: {room.get('title', 'Untitled')} | ID: {room.get('id')}")


def select_room(rooms):
    while True:
        name = input("Enter the room name (or part of it): ").strip()
        for room in rooms:
            if name.lower() in room["title"].lower():
                print(f"Room selected: {room.get('title', 'Untitled')} | ID: {room.get('id')}")
                return room["id"]
            
        print("Room not found. Please try again.")
        select_room(rooms)


def get_latest_message(token, room_id):
    url = "https://webexapis.com/v1/messages"
    params = {{"roomId": room_id, "max": 1}}
    headers = {"Authorization": token}
    
    
    try:
        response = requests.get(url, headers=headers, params=params)
        


        if response.status_code != 200:
            return None, None

        data = response.json().get("items", [])

        if not data:
            return None, None

        latest = data[0]
        return latest.get("id"), latest.get("text", "")
    
    except requests.RequestException as error:
            print("Error fetching latest message:", error)
            return None, None


def send_message(token, room_id, message):
    url = "https://webexapis.com/v1/messages"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    data = {
        "roomId": room_id,
        "text": message
    }
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        
        if response.status_code != 200:
            print("Error sending message:", response.status_code)
            print("Response:", response.text)
            
    except requests.RequestException as error:
        print("Unable to send message:", error)

# =========================
# WEATHER FUNCTIONS
# =========================
def get_city_coordinates(city, api_key):
    url = #complete the URL to fetch city coordinates from OpenWeatherMap API
    params = #complete the params dictionary to include the city name, limit, and the API key
    response = requests.#complete(url, params=params)

    if response.status_code != 200:
        return None

    data = response.json()
    return data[0] if data else None


def get_weather(city, api_key):
    location = get_city_coordinates(city, api_key)

    if not location:
        return #complete the return statement to indicate that the city was not found

    url = #complete the URL to fetch weather data from OpenWeatherMap API
    params = #complete the params dictionary to include the latitude, longitude, units as metric, and the API key

    response = requests.#complete(url, params=params)

    if response.status_code != 200:
        return #complete the return statement to indicate that the wheather weather data retrieved or not

    weather = response.json()

    return (
        #complete the return statement to format and return the weather information such as including city name, country, temperature, weather description, humidity, and wind speed
    )

# =========================
# ISS FUNCTIONS
# =========================
def reverse_geocode(lat, lon, api_key):
    url = #complete the URL to fetch reverse geocoding data from OpenWeatherMap API
    params = #complete the params dictionary to include the latitude, longitude, limit, and the API key

    response = requests.#complete(url, params=params)

    if response.status_code != 200:
        return None

    data = response.json()
    return data[0] if data else None


def get_iss_location(api_key):
    url = #complete the URL to fetch ISS current location from the Open Notify API

    response = requests.#complete(#complete)

    if response.status_code != 200:
        return #complete the return statement to indicate whether ISS location retrieved or not

    data = response.json()

    lat = data[#complete][#complete]
    lon = data[#complete][#complete]

    location = reverse_geocode(lat, lon, api_key)

    place = "Over Ocean / No Nearby City"

    if location:
        place = #

    return (
        #complete the return statement to format and return the ISS location information including latitude, longitude, and place name
    )

# =========================
# MAIN BOT LOGIC
# =========================
def main():

    token = get_webex_token()

    weather_key = get_api_key(
        "Weather API key",
        "YOUR_OPENWEATHER_API_KEY"
    )

    rooms = get_rooms(token)

    if not rooms:
        print(#complete the print statement )
        return

    print_rooms(rooms)
    room_id = select_room(rooms)

    last_message_id, _ = get_latest_message(token, room_id)

    while True:

        message_id, message_text = get_latest_message(token, room_id)

        if message_id and message_id != last_message_id:

            last_message_id = message_id

            print(#complete the print statement to display the received message text)

            if not message_text.startswith(#complete):
                continue

            if message_text.lower() == "/help":
                send_message(
                    token,
                    room_id,
                    "/weather <city>\n/iss\n/help\n/quit"
                )

            elif message_text.lower().startswith(#complete):

                parts = message_text.split(maxsplit=1)

                if len(parts) < 2:
                    send_message(token, room_id, "Usage: /weather <city>")
                else:
                    city = parts[1]
                    send_message(token, room_id, get_weather(city, weather_key))

            elif message_text.lower() == "#complete":
                send_message(token, room_id, get_iss_location(weather_key))

            elif message_text.lower() == "#complete":
                send_message(token, room_id, "AstroBot shutting down.")
                break

            else:
                send_message(token, room_id, "Unknown command. Use /help")

        time.sleep(5)


if __name__ == '__main__':
    main()
