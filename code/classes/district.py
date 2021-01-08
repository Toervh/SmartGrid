import json

class District:
    def __init__(self, houses, batteries):
        self.houses = houses
        self.batteries = batteries
        self.costs_shared = None
