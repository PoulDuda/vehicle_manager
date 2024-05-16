import requests
from src.function import distance, find_nearest


class Vehicle:
    def __init__(self, id: int, name: str, model: str, year: int, color: str,
                 price: int, latitude: float, longitude: float):
        self.id = id
        self.name = name
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f'<Vehicle: {self.name} {self.model} {self.year} {self.color} {self.price}>'


class VehicleManger:
    def __init__(self, url: str):
        self.url = url

    def get_vehicles(self):
        try:
            response = requests.get(self.url + '/vehicles')
            if response.status_code == 200:
                return [Vehicle(**vehicle) for vehicle in response.json()]
            else:
                response.raise_for_status()
        except requests.exceptions.RequestException as exception:
            return {'data': f'Error: {exception}'}

    def get_vehicle(self, vehicle_id):
        try:
            response = requests.get(self.url + f'/vehicles/{vehicle_id}')
            if response.status_code == 200:
                return Vehicle(**response.json())
            elif response.status_code == 404:
                return {'data': f'Error: Vehicle {vehicle_id} not found'}
            else:
                response.raise_for_status()
        except requests.exceptions.RequestException as exception:
            return {'data': f'Error: {exception}'}

    def filter_vehicles(self, params: dict):
        try:
            data = []
            response = requests.get(self.url + '/vehicles')
            if response.status_code == 200:
                for vehicle in response.json():
                    for key, val in params.items():
                        if vehicle[key] == val:
                            data.append(Vehicle(**vehicle))
                if data is []:
                    return {'data': 'There is no vehicle with your params'}
                return data
            else:
                response.raise_for_status()
        except requests.exceptions.ConnectionError:
            return {'data': 'Connection Error'}

    def delete_vehicle(self, vehicle_id: int):
        try:
            response = requests.delete(self.url + f'/vehicles/{vehicle_id}')
            if response.status_code == 204:
                return {'data': 'Vehicle deleted'}
            elif response.status_code == 404:
                return {'data': 'Vehicle not found'}
            else:
                response.raise_for_status()
        except requests.exceptions.ConnectionError:
            return {'data': 'Connection Error'}


    def update_vehicle(self, vehicle_id: int, params: dict):
        try:
            response = requests.put(self.url + f'/vehicles/{vehicle_id}', json=params)
            if response.status_code == 200:
                return Vehicle(**response.json())
            elif response.status_code == 404:
                return {'data': 'Vehicle not found'}
            else:
                response.raise_for_status()
        except requests.exceptions.RequestException as exception:
            return {'data': f'Error: {exception}'}

    def add_vehicle(self, vehicle: Vehicle):
        try:
            response = requests.post(self.url + '/vehicles', json=vars(vehicle))
            if response.status_code == 201:
                return vehicle
            else:
                response.raise_for_status()
        except requests.exceptions.RequestException as exception:
            return {'data': f'Error: {exception}'}

    def get_distance(self, id1: int, id2: int):
        try:
            r1 = requests.get(self.url + f'/vehicles/{id1}')
            r2 = requests.get(self.url + f'/vehicles/{id2}')
            if r1.status_code == 200 and r2.status_code == 200:
                coord = [r1.json()["latitude"], r1.json()["longitude"],
                         r2.json()["latitude"], r2.json()["longitude"]]
                return distance(*coord)
        except requests.exceptions.RequestException as exception:
            return {'data': f'Error: {exception}'}

    def get_nearest_vehicle(self, vehicle_id: int):
        try:
            r1 = requests.get(self.url + f'/vehicles/{vehicle_id}')
            if r1.status_code == 200:
                coord = [r1.json()["latitude"], r1.json()["longitude"]]
                r2 = requests.get(self.url + f'/vehicles')
                nearest_id = find_nearest(*coord, r2.json())
                for vehicle in r2.json():
                    if vehicle["id"] == nearest_id:
                        return Vehicle(**vehicle)
            else:
                r1.raise_for_status()
        except requests.exceptions.RequestException as exception:
            return {'data': f'Error: {exception}'}
