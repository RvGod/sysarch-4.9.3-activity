import requests
import urllib.parse
from config import route_url

def get_route(orig, dest, key, vehicle):
    params = {
        "key": key,
        "vehicle": vehicle,
        "algorithm": "alternative_route",
        "point": [
            f"{orig[1]},{orig[2]}",
            f"{dest[1]},{dest[2]}"
        ]
    }

    query = urllib.parse.urlencode(params, doseq=True)
    url = route_url + "?" + query

    try:
        response = requests.get(url)
    except requests.exceptions.RequestException:
        print("Connection error")
        return 0, {"message": "Connection error"}, url

    try:
        data = response.json()
    except:
        data = {"message": "Invalid API response"}

    return response.status_code, data, url
