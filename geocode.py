def get_route(orig, dest, key, vehicle):
    op = f"&point={orig[1]}%2C{orig[2]}"
    dp = f"&point={dest[1]}%2C{dest[2]}"

    params = {
        "key": key,
        "vehicle": vehicle,
        "algorithm": "alternative_route"  # NEW FEATURE
    }

    paths_url = route_url + urllib.parse.urlencode(params) + op + dp
    response = requests.get(paths_url)
    return response.status_code, response.json(), paths_url


# Inside your main loop:
if paths_status == 200:
    km, miles = convert_distance(paths_data["paths"][0]["distance"])
    hr, min, sec = format_time(paths_data["paths"][0]["time"])

    print(f"Distance Traveled: {miles:.1f} miles / {km:.1f} km")
    print(f"Trip Duration: {hr:02d}:{min:02d}:{sec:02d}")
    print("=================================================")

    for instr in paths_data["paths"][0]["instructions"]:
        path_text = instr["text"]
        dist_km, dist_miles = convert_distance(instr["distance"])
        print(f"{path_text} ({dist_km:.1f} km / {dist_miles:.1f} miles)")

    # Cost estimation
    fuel_price = 0
    if vehicle == "car":
        try:
            fuel_price = float(input("Enter fuel price per liter (₱): "))
        except ValueError:
            print("Invalid input, assuming ₱0.")

    trip_cost = estimate_cost(km, vehicle, fuel_price)
    print(f"Estimated Trip Cost: ₱{trip_cost:.2f}")
    print("=============================================")

    # Save history
    history.append({"from": orig[3], "to": dest[3], "distance": km})

    # Print route history once
    print("\nRoute History:")
    for h in history:
        print(f"{h['from']} -> {h['to']} ({h['distance']:.1f} km)")
    print("=============================================")
