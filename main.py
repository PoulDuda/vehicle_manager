from src.vehile_manager import VehicleManger, Vehicle


if __name__ == '__main__':
    manager = VehicleManger(url="https://test.tspb.su/test-task")

    print('All vehicles from source:')
    print(manager.get_vehicles())
    print()

    print('Vehicle by id:')
    print(manager.get_vehicle(2))
    print()

    print('Filter function by color: ')
    print(manager.filter_vehicles(params={"color": "red"}))
    print()

    print('Deleting vehicle by id:')
    print(manager.delete_vehicle(vehicle_id=2))
    print()

    print('Updating vehicle by id:')
    print(manager.update_vehicle(vehicle_id=1, params={"color": "black"}))
    print()

    print('Adding vehicle:')
    print(manager.add_vehicle(vehicle=Vehicle(
            id=1,
            name='Toyota',
            model='Camry',
            year=2021,
            color='red',
            price=21000,
            latitude=55.753215,
            longitude=37.620393
            )
    ))
    print()

    print('Check distance between two vehicles:')
    print(manager.get_distance(id1=8, id2=6))
    print()

    print('Get the nearest vehicle:')
    print(manager.get_nearest_vehicle(1))
    print()
