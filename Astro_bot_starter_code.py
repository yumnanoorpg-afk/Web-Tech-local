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
    elif choice == "y":
        return "Bearer N2Q3YTc0ZTItMjVjNy00YzUxLTg5MzEtYWE5NGYxYjc0MmUwY2JlMWI1MjMtMTJj_PE93_c18e13ae-5575-4bc0-ae01-e48905f14f17"  # Replace TToken with your actual hard-coded token
    else:
        print("Invalid choice. Please enter 'y' or 'n'.")
        return get_webex_token()
    
    
#ask the user for the Weather API key or use a hard-coded key. Return the key in the format "Bearer <key>"
def get_api_key(prompt, hardcoded_key):
    choice = input(f"Use hard-coded {prompt}? (y/n): ").lower().strip()

    if choice == "n":
        return input(f"Enter your {prompt}: ").strip()
    elif choice == "y":
        return "Bearer 666194cbf25284960e5349401a9125b3"  # Replace Api Key with your actual hard-coded API key
    else:
        print("Invalid choice. Please enter 'y' or 'n'.")
        return get_api_key(prompt, hardcoded_key)


# =========================
# WEBEX FUNCTIONS
# =========================

def get_rooms(token):
    url = "https://webexapis.com/v1/rooms"
    headers = {"Authorization": token}

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code != 200:
            print("Error fetching rooms:", response.status_code)
            return []

        return response.json().get("items", [])

    except (requests.RequestException, ValueError) as error:
        print("Unable to retrieve rooms:", error)
        return []


def print_rooms(rooms):
    for room in rooms:
        print(f"Room: {room.get('title', 'Untitled')} | ID: {room.get('id')}")


def select_room(rooms):
    while True:
        name = input("Enter the room name (or part of it): ").strip()

        for room in rooms:
            if name and name.lower() in room.get("title", "").lower():
                print(f"Selected room: {room.get('title')}")
                return room["id"]

        print("Room not found. Please try again.")
        return select_room(rooms)


def get_latest_message(token, room_id):
    url = "https://webexapis.com/v1/messages"
    params = {"roomId": room_id, "max": 1}
    headers = {"Authorization": token}

    try:
        response = requests.get(
            url, headers=headers, params=params, timeout=10
        )

        if response.status_code != 200:
            print("Error fetching messages:", response.status_code)
            return None, None

        data = response.json().get("items", [])

        if not data:
            return None, None

        latest = data[0]
        return latest.get("id"), latest.get("text", "")

    except (requests.RequestException, ValueError) as error:
        print("Unable to retrieve messages:", error)
        return None, None


def send_message(token, room_id, message):
    url = "https://webexapis.com/v1/messages"

    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }

    data = {
        "roomId": room_id,
        "text": str(message)
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            data=json.dumps(data),
            timeout=10
        )

        if response.status_code not in (200, 201):
            print("Error sending message:", response.status_code)
            print(response.text)

    except requests.RequestException as error:
        print("Unable to send message:", error)


# =========================
# WEATHER FUNCTIONS
# =========================

def get_city_coordinates(city, api_key):
    url = "https://api.openweathermap.org/geo/1.0/direct"

    params = {
        "q": city,
        "limit": 1,
        "appid": api_key
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code != 200:
            print("Geocoding error:", response.status_code)
            return None

        data = response.json()
        return data[0] if data else None

    except (requests.RequestException, ValueError) as error:
        print("Unable to find city coordinates:", error)
        return None


def get_weather(city, api_key):
    location = get_city_coordinates(city, api_key)

    if not location:
        return f"Could not find weather information for {city}."

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "lat": location["lat"],
        "lon": location["lon"],
        "units": "metric",
        "appid": api_key
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code != 200:
            return "Unable to retrieve weather data at the moment."

        weather = response.json()

        city_name = weather.get("name", city)
        country = weather.get("sys", {}).get("country", "")
        temperature = weather.get("main", {}).get("temp", "N/A")
        description = (
            weather.get("weather", [{}])[0].get("description", "Unknown")
        )
        humidity = weather.get("main", {}).get("humidity", "N/A")
        wind_speed = weather.get("wind", {}).get("speed", "N/A")

        return (
            f"Weather for {city_name}, {country}\n"
            f"Temperature: {temperature}°C\n"
            f"Conditions: {description}\n"
            f"Humidity: {humidity}%\n"
            f"Wind speed: {wind_speed} m/s"
        )

    except (requests.RequestException, ValueError, KeyError) as error:
        print("Weather error:", error)
        return "An error occurred while retrieving weather information."


# =========================
# ISS FUNCTIONS
# =========================

def reverse_geocode(lat, lon, api_key):
    url = "https://api.openweathermap.org/geo/1.0/reverse"

    params = {
        "lat": lat,
        "lon": lon,
        "limit": 1,
        "appid": api_key
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code != 200:
            return None

        data = response.json()
        return data[0] if data else None

    except (requests.RequestException, ValueError) as error:
        print("Reverse geocoding error:", error)
        return None


def get_iss_location(api_key):
    url = "http://api.open-notify.org/iss-now.json"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return "Unable to retrieve the ISS location at the moment."

        data = response.json()

        if data.get("message") != "success":
            return "The ISS API did not return a successful response."

        position = data.get("iss_position", {})
        lat = position.get("latitude")
        lon = position.get("longitude")

        if lat is None or lon is None:
            return "The ISS location data is incomplete."

        location = reverse_geocode(lat, lon, api_key)

        place = "Over ocean / no nearby city"

        if location:
            place = location.get("name") or location.get(
                "state"
            ) or location.get("country") or place

        timestamp = data.get("timestamp")
        time_text = ""

        if timestamp is not None:
            time_text = datetime.fromtimestamp(
                int(timestamp), timezone.utc
            ).strftime("%Y-%m-%d %H:%M:%S UTC")

        return (
            "Current ISS location\n"
            f"Latitude: {lat}\n"
            f"Longitude: {lon}\n"
            f"Nearest identified place: {place}\n"
            f"Timestamp: {time_text or 'Unavailable'}"
        )

    except (requests.RequestException, ValueError, TypeError) as error:
        print("ISS location error:", error)
        return "An error occurred while retrieving the ISS location."


# =========================
# EXTENDED FEATURE: AIR QUALITY
# =========================

def get_air_quality(city, api_key):
    location = get_city_coordinates(city, api_key)

    if not location:
        return f"Could not find the location of {city}."

    url = "https://api.openweathermap.org/data/2.5/air_pollution"

    params = {
        "lat": location["lat"],
        "lon": location["lon"],
        "appid": api_key
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code != 200:
            return "Unable to retrieve air quality data."

        data = response.json()
        items = data.get("list", [])

        if not items:
            return "No air quality data is available for this location."

        result = items[0]
        aqi = result.get("main", {}).get("aqi")
        components = result.get("components", {})

        # OpenWeatherMap AQI scale: 1 (best) to 5 (worst)
        aqi_labels = {
            1: "Good",
            2: "Fair",
            3: "Moderate",
            4: "Poor",
            5: "Very poor"
        }

        label = aqi_labels.get(aqi, "Unknown")

        return (
            f"Air quality for {city}\n"
            f"Air Quality Index: {aqi} ({label})\n"
            f"PM2.5: {components.get('pm2_5', 'N/A')} µg/m³\n"
            f"PM10: {components.get('pm10', 'N/A')} µg/m³"
        )

    except (requests.RequestException, ValueError, KeyError) as error:
        print("Air quality error:", error)
        return "An error occurred while retrieving air quality data."


# =========================
# MAIN BOT LOGIC
# =========================

def main():
    token = get_webex_token()

    if not token:
        print("Configure a valid Webex access token before continuing.")
        return

    weather_key = get_api_key(
        "Weather API key",
        "666194cbf25284960e5349401a9125b3"
    )

    if not weather_key:
        print("Configure a valid OpenWeatherMap API key before continuing.")
        return

    rooms = get_rooms(token)

    if not rooms:
        print("No rooms found, or unable to access Webex rooms.")
        return

    print_rooms(rooms)
    room_id = select_room(rooms)

    last_message_id, _ = get_latest_message(token, room_id)

    print("AstroBot is running. Use /help to see commands.")

    while True:
        message_id, message_text = get_latest_message(token, room_id)

        if message_id and message_id != last_message_id:
            last_message_id = message_id
            message_text = (message_text or "").strip()

            print("Received message:", message_text)

            # Ignore messages that are not bot commands.
            if not message_text.startswith("/"):
                time.sleep(5)
                continue

            command = message_text.lower()

            if command == "/help":
                send_message(
                    token,
                    room_id,
                    "AstroBot commands:\n"
                    "/weather <city> - Get current weather\n"
                    "/iss - Get the current ISS location\n"
                    "/air <city> - Get air quality\n"
                    "/help - Show this help message\n"
                    "/quit - Shut down AstroBot"
                )

            elif command == "/iss":
                send_message(
                    token, room_id, get_iss_location(weather_key)
                )

            elif command == "/quit":
                send_message(token, room_id, "AstroBot shutting down.")
                break

            elif command.startswith("/weather"):
                parts = message_text.split(maxsplit=1)

                if len(parts) < 2 or parts[0].lower() != "/weather":
                    send_message(
                        token, room_id, "Usage: /weather <city>"
                    )
                else:
                    city = parts[1].strip()
                    send_message(
                        token, room_id, get_weather(city, weather_key)
                    )

            elif command.startswith("/air"):
                parts = message_text.split(maxsplit=1)

                if len(parts) < 2 or parts[0].lower() != "/air":
                    send_message(
                        token, room_id, "Usage: /air <city>"
                    )
                else:
                    city = parts[1].strip()
                    send_message(
                        token, room_id,
                        get_air_quality(city, weather_key)
                    )

            else:
                send_message(
                    token, room_id, "Unknown command. Use /help"
                )

        time.sleep(5)


if __name__ == "__main__":
    main()
