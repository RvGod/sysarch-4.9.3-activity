def format_time(ms):
    sec = int(ms/1000 % 60)
    min = int(ms/1000/60 % 60)
    hr = int(ms/1000/60/60)
    return hr, min, sec

def convert_distance(meters):
    km = meters / 1000
    miles = km / 1.61
    return km, miles