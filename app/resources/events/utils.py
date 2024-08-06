# app/resources/events/utils.py

import math
from fastapi import HTTPException


def parse_geolocation(geolocation: str):
    """Parse geolocation string to extract latitude and longitude as floats."""
    try:
        lat_str, lon_str = geolocation.split(',')
        return float(lat_str), float(lon_str)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid geolocation format")


def haversine_distance(lat1, lon1, lat2, lon2):
    """Calculate the Haversine distance between two points on the Earth."""
    # Radius of the Earth in kilometers
    R = 6371.0

    # Convert latitude and longitude from degrees to radians
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    # Haversine formula
    a = math.sin(delta_phi / 2.0) ** 2 + \
        math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2.0) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distance in kilometers
    distance = R * c
    return distance

def calculate_distance(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1 
    dlon = lon2 - lon1 
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))

    # Radius of earth in kilometers is 6371
    km = 6371 * c
    return km
