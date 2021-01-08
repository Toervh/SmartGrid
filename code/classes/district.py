import json

class District:
    def __init__(self, houses, batteries):
        self.houses = houses
        self.batteries = batteries
        self.costs_shared = None

    def print_district(self):
        for battery in self.batteries:
            print(f"battery ID: {battery.id}")
            print(f"battery x coordinate: {battery.x_coordinate}")
            print(f"battery y coordinate: {battery.y_coordinate}")
            print(f"battery capacity: {battery.capacity}")
            print(f"list of conncted houses: {battery.houses}")

        for house in self.houses:
            print(f"house id: {house.id}")
            print(f"house x coordinate: {house.x_coordinate}")
            print(f"house y coordinate: {house.y_coordinate}")
            print(f"house output: {house.output}")
            print(f"house connected battery ID: {house.connected_battery}")
            print(f"cables: {house.cables}")