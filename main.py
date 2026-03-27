from config import key
from geocode import geocoding
from routing import get_route

while True:
    print("\n+++++++++++++++++++++++++++++++++++++++++++++")
    print("Vehicle profiles available on Graphhopper:")
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    print("car, bike, foot")
    print("+++++++++++++++++++++++++++++++++++++++++++++")

    profile = ["car", "bike", "foot"]
    vehicle = input("Enter a vehicle profile from the list above: ")

    if vehicle == "quit" or vehicle == "q":
        break
    elif vehicle not in profile:
        vehicle = "car"
        print("No valid vehicle profile was entered. Using the car profile.")

    loc1 = input("Starting Location: ")
    if loc1 in ["quit", "q"]:
        break
    orig = geocoding(loc1, key)

    loc2 = input("Destination: ")
    if loc2 in ["quit", "q"]:
        break
    dest = geocoding(loc2, key)

    print("=================================================")

    if orig[0] == 200 and dest[0] == 200:
        paths_status, paths_data, paths_url = get_route(orig, dest, key, vehicle)

        print("Routing API Status: " + str(paths_status) +
              "\nRouting API URL:\n" + paths_url)

        print("=================================================")
        print("Directions from " + orig[3] + " to " + dest[3] + " by " + vehicle)
        print("=================================================")

        if paths_status == 200:
            miles = (paths_data["paths"][0]["distance"]) / 1000 / 1.61
            km = (paths_data["paths"][0]["distance"]) / 1000

            sec = int(paths_data["paths"][0]["time"]/1000 % 60)
            min = int(paths_data["paths"][0]["time"]/1000/60 % 60)
            hr = int(paths_data["paths"][0]["time"]/1000/60/60)

            print("Distance Traveled: {0:.1f} miles / {1:.1f} km".format(miles, km))
            print("Trip Duration: {0:02d}:{1:02d}:{2:02d}".format(hr, min, sec))
            print("=================================================")

            for each in range(len(paths_data["paths"][0]["instructions"])):
                path = paths_data["paths"][0]["instructions"][each]["text"]
                distance = paths_data["paths"][0]["instructions"][each]["distance"]

                print("{0} ( {1:.1f} km / {2:.1f} miles )".format(
                    path, distance/1000, distance/1000/1.61))

            print("=============================================")
        else:
            print("Error message: " + paths_data["message"])
            print("*************************************************")