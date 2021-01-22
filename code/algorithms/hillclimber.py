from code.algorithms.randomize import random_assignment
from code.classes.district import District
from code.functions.lay_cables import create_cable
from code.functions.find_closest_cable import find_closest_cable
import copy
import random


def find_random_cable(available_batteries):
    random_battery = random.choice(available_batteries)
    x_coordinate = random_battery.x_coordinate
    y_coordinate = random_battery.y_coordinate
    random_point = (x_coordinate, y_coordinate)
    return random_point

def HillClimber(list_house_objects, list_battery_objects):
    id = 1

    d = District(id, list_house_objects, list_battery_objects)
    climber_district = random_assignment(d)
    copied_district = copy.deepcopy(climber_district)
    
    list_batteries = []
    for battery in copied_district.batteries:
        list_batteries.append(battery)
    list_batteries_copy = copy.deepcopy(list_batteries)

    for house in copied_district.houses:
        N = 0
        while True:
            # haal dit huis uit zn batterij etc
            house.remove_connected_battery()
            house.remove_cables()
            for battery in list_batteries_copy:
                try:
                    battery.houses.remove(house.id)
                    battery.houses_objects.remove(house)
                except ValueError:
                    continue
            
            

            # kies uit alle mogelijk aansluitpunten (gepruned op dichtsbijzijnd?) een aansluitpunt
            # sluit deze optie weer aan
            
            
            # check of de kosten hoger zijn gewordenvvv

            if climber_district.costs_shared < copied_district.costs_shared:   #of kabelkost?
                current_district_iteration = copy.deepcopy(copied_district)
                climber_district = current_district_iteration
            
            elif climber_district.costs_shared > copied_district.costs_shared:
                # maak ongedaan
                N+=1
            
            elif climber_district.costs_shared > copied_district.costs_shared and N > 10:
                # maak ongedaan
                break

    return climber_district