#liters h^-1 to m^3 s^1
def litres_to_cubic_meters(litres_per_hour):
    return litres_per_hour / 1000


def hours_to_seconds(hours):
    return hours / 3600


def litres_per_hour_to_cubic_metre_per_sec(value):
    liters_to_cubic_metres = litres_to_cubic_meters(value) # lph / 1000
    cubic_metres_per_second = hours_to_seconds(liters_to_cubic_metres) # cbmps / 3600
    return cubic_metres_per_second


print(litres_per_hour_to_cubic_metre_per_sec(57))

# liters min^-1 to m^3 s^1
def litres_to_cubic_meters(litres_per_hour):
    return litres_per_hour / 1000


def minutes_to_seconds(minutes):
    return minutes / 60


def litres_per_min_to_cubic_metre_per_sec(value):
    liters_to_cubic_metres = litres_to_cubic_meters(value) # lph / 1000
    cubic_metres_per_second = minutes_to_seconds(liters_to_cubic_metres) # cbmps / 3600
    return cubic_metres_per_second


print(litres_per_hour_to_cubic_metre_per_sec(57))
