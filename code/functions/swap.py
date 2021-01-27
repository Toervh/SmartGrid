from code.functions.find_closest_cable import find_closest_cable
from code.functions.lay_cables import create_cable
import copy
import random

def swap(district):
    # swapped = False
    old_cost = district.costs_shared
    #print(f"house: {house.id},  cheapest connection: {old_cost}")
    swap_district = copy.deepcopy(district)
    new_cost = swap_district.costs_shared
    #list_available_houses = swap_capacity(copy_district, copy_house)


    for house in swap_district.houses:
        random_house = random.choice(list(swap_district.houses))
        
        random_battery = random_house.connected_battery
        old_battery = house.connected_battery

        random_battery_cables = list(set(random_battery.cables).difference(random_house.cables))

        random_battery.cables = random_battery_cables
        random_house.cables = []
        for element in random_battery_cables:
            del element


        old_battery_cables = list(set(old_battery.cables).difference(house.cables))

        old_battery.cables = old_battery_cables
        for element in old_battery_cables:
            del element
        
        house.cables = []

        house.connected_battery = random_battery
        random_house.connected_battery = old_battery

        closest_cable = find_closest_cable(random_battery, house)
        create_cable(house.x_coordinate, house.y_coordinate, closest_cable.x_coordinate, closest_cable.y_coordinate, swap_district, house, random_battery)

        closest_cable_2 = find_closest_cable(old_battery, random_house)
        create_cable(random_house.x_coordinate, random_house.y_coordinate, closest_cable_2.x_coordinate, closest_cable_2.y_coordinate, swap_district, random_house, old_battery)

        if new_cost < old_cost:
            print("over naar nieuw district")
            print(f"New Cost: {new_cost}")
            print(f"Old cost: {old_cost}")
            swapped = True
            old_cost = new_cost
            district = swap_district
        else:  
            swap_district = district

    return district
