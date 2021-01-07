import json

class District:
    def __init__(self, id, houses, batteries):
        self.id = id
        self.houses = houses
        self.batteries = batteries
        self.costs_shared = None

    #def __repr__(self):
        #return json.dumps({"district":self.id, "costs-shared": self.costs_shared})

    # def json_output(self, object):
    #     data = json.dumps(object)
    #     print(data)

    # def toJSON(self):
    #     return json.dumps(self, default=lambda o: o.__dict__,
    #                       sort_keys=True, indent=4)


    #     with open('data.txt', 'w') as outfile:
    #         json.dump(data, outfile)
        # print(data)
        # for battery in self.batteries:
        #     data['capacity'] = battery.capacity
        #     data['location'] = battery.x_coordinate,battery.y_coordinate
        #     data['houses'] = []
        #     for house in houses:
        #         if house.connected_battery == battery.id:
        #             #data['houses'].append({'location': house.x_coordinate,house.y_coordinate, 'output': house.output, 'cables': house.cables})
        #             pass
