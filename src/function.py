from math import sin, cos, sqrt, radians, asin


def distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    R = 6_371_000

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    d_lon = lon2 - lon1
    d_lat = lat2 - lat1

    x = sin(d_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(d_lon / 2) ** 2
    return 2 * R * asin(sqrt(x))


def find_nearest(lat: float, lon: float, json: dict) -> int:
    distances = dict()
    for vehicle in json:

        dist = distance(lat, lon, vehicle['latitude'], vehicle['longitude'])
        if dist == 0.0:
            continue
        else:
            distances[vehicle['id']] = dist
    return min(distances.items(), key=lambda x: x[1])[0]
