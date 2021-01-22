from code.algorithms.randomize import random_assignment
from code.classes.district import District
from code.functions.lay_cables import create_cable
from code.functions.find_closest_cable import find_closest_cable
import copy
import random


def find_random_cable(available_batteries):
    random_cable_list = []
    random_cable_list.append(())
    random_point = random.choice(available_batteries)
    return random_point

def HillClimber(list_house_objects, list_battery_objects):
    id = 1

    d = District(id, list_house_objects, list_battery_objects)
    randomized_district = random_assignment(d)
    copied_district = copy.deepcopy(randomized_district)
    
    list_batteries = []
    for battery in copied_district.batteries:
        list_batteries.append(battery)
    list_batteries_copy = copy.deepcopy(list_batteries)

    for house in copied_district.houses:
        N = 0
        while True:
            climbing_copy = copy.deepcopy(copied_district)
            new_random_cable = find_random_cable(list_batteries_copy)
            
            if copied_district.costs_shared < climbing_copy.costs_shared:   #of kabelkost?
                copied_district = climbing_copy
                create_cable(house.x_coordinate, house.y_coordinate, district, house)
            elif copied_district.costs_shared > climbing_copy.costs_shared:
                N+=1
            elif copied_district.costs_shared > climbing_copy.costs_shared and N > 10:
                break

    return climbing_copy