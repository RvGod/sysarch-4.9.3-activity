def format_time(ms):
    sec = int(ms / 1000 % 60)
    min = int(ms / 1000 / 60 % 60)
    hr = int(ms / 1000 / 60 / 60)
    return hr, min, sec

def convert_distance(meters):
    km = meters / 1000
    miles = km / 1.61
    return km, miles

def estimate_cost(distance_km, vehicle_type, fuel_price=0):
    if vehicle_type == "car":
        fuel_efficiency = 12
        cost = (distance_km / fuel_efficiency) * fuel_price

    elif vehicle_type == "bike":
        cost = 0

    else:
        cost = 0

    return cost
