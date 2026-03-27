import requests
import urllib.parse
from config import route_url

def get_route(orig, dest, key, vehicle):
    op = "&point=" + str(orig[1]) + "%2C" + str(orig[2])
    dp = "&point=" + str(dest[1]) + "%2C" + str(dest[2])

    paths_url = route_url + urllib.parse.urlencode({
        "key": key,
        "vehicle": vehicle,
        "algorithm": "alternative_route" #NEW FEATURE
    }) + op + dp

    response = requests.get(paths_url)
    return response.status_code, response.json(), paths_url
