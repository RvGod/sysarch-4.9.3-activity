from config import key
from geocode import geocoding
from routing import get_route
import webbrowser


history = [] 

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
       for i, path in enumerate(paths_data["paths"]):
            km = path["distance"] / 1000
            miles = km / 1.61

            hr = int(path["time"]/1000/60/60)
            min = int(path["time"]/1000/60 % 60)
            sec = int(path["time"]/1000 % 60)

            print("==============================================")
            print(f"Route {i+1}:")
            print("Distance: {0:.1f} km / {1:.1f} miles".format(km, miles))
            print("Trip Duration: {0:02d}:{1:02d}:{2:02d}".format(hr, min, sec))
            print("==============================================")

            for instr in path["instructions"]:
                step = instr["text"]
                dist = instr["distance"]
                print("{0} : {1:.1f} km / {2:.1f} miles".format(
                    step, dist/1000, dist/1000/1.61))

            history.append({
                "from": orig[3],
                "to": dest[3],
                "distance": km
            })

            mode_map = {
                "car": "driving",
                "bike": "bicycling",
                "foot": "walking"
            }

            travel_mode = mode_map.get(vehicle, "driving")

            maps_url = f"https://www.google.com/maps/dir/?api=1&origin={orig[1]},{orig[2]}&destination={dest[1]},{dest[2]}&travelmode={travel_mode}"

            webbrowser.open(maps_url)
            print("Open in browser:", maps_url)

            print("Distance Traveled: {0:.1f} miles / {1:.1f} km".format(miles, km))
            print("Trip Duration: {0:02d}:{1:02d}:{2:02d}".format(hr, min, sec))
            print("=================================================")

            for each in range(len(paths_data["paths"][0]["instructions"])):
                path = paths_data["paths"][0]["instructions"][each]["text"]
                distance = paths_data["paths"][0]["instructions"][each]["distance"]

                print("{0} ( {1:.1f} km / {2:.1f} miles )".format(
                    path, distance/1000, distance/1000/1.61))
                print("\nRoute History:")

                for h in history:
                    print(f"{h['from']} -> {h['to']} ({h['distance']:.1f} km)")
            print("=============================================")
        else:
            print("Error message: " + paths_data["message"])
            print("*************************************************")
