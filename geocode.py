import requests
import urllib.parse
from config import geocode_url

def geocoding(location, key):
    while location.strip() == "":
        location = input("Enter the location again: ")

    url = geocode_url + "?" + urllib.parse.urlencode({
        "q": location,
        "limit": 1,
        "key": key
    })

    try:
        response = requests.get(url)
    except requests.exceptions.RequestException:
        print("Connection error")
        return 0, None, None, location

    try:
        json_data = response.json()
    except:
        print("Invalid JSON response")
        return response.status_code, None, None, location

    if response.status_code == 200 and json_data.get("hits"):
        hit = json_data["hits"][0]

        lat = hit["point"]["lat"]
        lng = hit["point"]["lng"]
        name = hit.get("name", location)

        country = hit.get("country", "")
        state = hit.get("state", "")

        new_loc = ", ".join(filter(None, [name, state, country]))

        print(f"Geocoding API URL for {new_loc}:\n{url}")

        return 200, lat, lng, new_loc

    else:
        print("Geocoding failed:", json_data.get("message", "Unknown error"))
        return response.status_code, None, None, location
