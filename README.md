# Web-Tech local


# 🚀 Space Bot API Investigation Sheet
**Total Marks: 40**

---
## Webex Messaging API (4 marks)
| Criteria | Details |
|---------|---------|
| API Base URL | `[https://webexapis.com/v1](https://webexapis.com/v1/messages/{messageId} \)` |
| Authentication Method | `Bearer <access_token>` |
| Endpoint to list rooms | `/rooms` |
| Endpoint to get messages | `/messages` |
| Endpoint to send message | `/messages` |
| Required headers | `Authorization: Bearer <token>, Content-Type: application/json` |
| Sample full GET or POST request | `GET rooms: curl -H "Authorization: Bearer <token>" https://webexapis.com/v1/rooms` |
---
## ISS Current Location API (2 marks)
| Criteria | Details |
|---------|---------|
| API Base URL | `http://api.open-notify.org` |
| Endpoint for current ISS location | `/iss-now.json` |
| Sample response format (example JSON) |
```json { "message": "success", "timestamp": 1596563200, "iss_position": { "latitude": "48.8584", "longitude": "2.2945" } }
```
|
---
## Geocoding API (4 marks)
| Criteria | Details |
|---------|---------|
| Provider used (Choose one) | **LocationIQ / Mapbox/ OpenWeatherMap other -provide
detail** |
| API Base URL | `http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}` |
| Endpoint for geocoding | `/geo/1.0/direct` |
| Endpoint for reverse geocoding | `/geo/1.0/reverse` |
| Authentication method | `key=<API_KEY>` |
| Required query parameters | `key, q ` |
| Sample request with latitude/longitude | `https://us1.locationiq.com/v1/reverse.php?key=YOUR_KEY&lat=51.5074&lon=-0.1278&format=json` |
| Sample JSON response (formatted example) |
```	
json { "place_id": "12345", "lat": "51.5074", "lon": "-0.1278", "display_name": "London, UK" }
```
|
---
## Weather API (3 marks)
| Criteria | Details |
|---------|---------|
| API Provider (Choose one) | **OpenWeather, OpenWeatherMap (or other – provide
details)** |
| API Base URL | `https://api.openweathermap.org/data/2.5` |
| Endpoint for current weather | `/weather` |
| Authentication method | `appid=<API_KEY>` |
| Required query parameters | `q (city) or lat/lon, appid` |
| Sample JSON response (formatted example) |
```json { "weather":[{"main":"Clouds"}], "main":{"temp":289.5}, "name":"London" }
```
|
---
## Epoch to Human Time Conversion (Python time module) (2 marks)
| Criteria | Details |
|---------|---------|
| Library used | `_______________________________` |
| Function used to convert epoch | `_______________________________` |
| Sample code to convert timestamp |
```
```
|
| Output (human-readable time) | `_______________________________` |
---
## Extended Feature API ( 3 marks)
| Criteria | Details |
|---------|---------|
| API Provider | 'openWeatherApi' |
| API Base URL | `https://api.openweathermap.org/data/2.5` |
| Endpoint | `/air_pollution` |
| Authentication method | `appid=<API_KEY>` |
| Required query parameters | `lat, lon, appid` |
| Sample JSON response (formatted example) |
```	
json { "coord": { "lon": -0.1278, "lat": 51.5074 }, "list": [ { "main": { "aqi": 2 }, "components": { "pm2_5": 4.2, "pm10": 7.1 } } ] }
```
|
---
## Evaluation – Web Architecture, MVC Design & Security
In this section, evaluate how web technologies, architecture, and design patterns
have been applied in your **AstroBot**. Your responses must relate directly to your
implementation and include reflection on your design decisions.
---
### Web Architecture – Client–Server Model (3 marks)
Explain how the client–server model applies to your AstroBot:
- Identify the **client**
- Identify the **server(s)**
- Describe how data flows between:
- User, AstroBot and APIs
Include a **simple block diagram** to illustrate this interaction.
#### Security Considerations: (3 marks )
- Consider but not limiting to secure handling of API keys and tokens, API rate
limiting, and Input validation (e.g., handling user commands safely), include
examples from code where necessary to illustrate.
---
### RESTful API Usage in Your Application (3 marks )
Explain how REST APIs are used in your AstroBot:
- Describe how HTTP methods (GET, POST) are used
- Explain how your bot interacts with APIs (Webex, Weather, ISS, Geocoding)
- Describe how JSON responses are received and processed
Note: Relate your explanation directly to your code for higher grade.
#### Security Considerations: (2 marks)
- Check response status codes, Handling invalid or unexpected API responses,
Avoiding excessive API calls
---
### MVC Design Pattern in AstroBot (3 Marks)
Explain how the **Model–View–Controller (MVC)** pattern applies to your solution:
Provide a short example based on your implementation
| Component | Description and Example (Relate to your Bot) |
|------------|----------------------------------|
| **Model** | |
| **View** | |
| **Controller** | |
---
### 🚀 Reflection and Evaluation ( 8 marks )
Reflect on your AstroBot (400 words):
- How effective is your bot in meeting the Astronomy Club’s needs?
- What design decisions worked well?
- What challenges did you face when integrating APIs?
- What security risks did you identify and how were they handled?
- How could your solution be improved in the future?
