import json

class District:
    def __init__(self, id, houses, batteries):
        self.id = id
        self.houses = houses
        self.batteries = batteries
        self.costs_shared = 0
        self.cables_coordinates = []

#Add cables function moved to cable.py
    # def add_cable(self, x_coordinate, y_coordinate, house):
    #     new_coordinates = (x_coordinate, y_coordinate)
    #     print(new_coordinates)
    #
    #     for cable in self.cables_coordinates:
    #         if new_coordinates == cable:
    #             pass
    #
    #     self.cables_coordinates.append((x_coordinate, y_coordinate))
    #     house.cables.append((x_coordinate, y_coordinate))
    #     self.costs_shared += 9


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

    def dict_me(self):
        district_list = []
        dict_district = {'district': self.id, 'costs-shared': self.costs_shared}
        district_list.append(dict_district)

        for battery in self.batteries:
            dict_battery = {'location': str(battery)}
            dict_battery['capacity'] = battery.capacity

            dict_battery['houses'] = []
            for house in battery.houses_objects:
                dict_house = {'location': str(house)}
                dict_house['output'] = house.output
                dict_battery['houses'].append(dict_house)

            district_list.append(dict_battery)

        with open('json.txt', 'w') as outfile:
            json.dump(district_list, outfile, indent=4)