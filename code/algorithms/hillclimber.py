from code.algorithms.randomize import random_assignment
from code.classes.district import District
import copy


def find_random_cable(house, available_batteries):
    random_cable_list = []
    start_x = house.x_coordinates
    start_y = house.y_coordinates
    random_cable_list.append((start_x, start_y))
    return random_cable_list

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
            
            new_random_cable = find_random_cable(house, available_batteries)
            
            if copied_district.costs_shared < climbing_copy.costs_shared:   #of kabelkost?
                copied_district = climbing_copy
            elif copied_district.costs_shared > climbing_copy.costs_shared:
                N+=1
            elif copied_district.costs_shared > climbing_copy.costs_shared and N > 10:
                break