from code.functions.find_closest_cable import find_closest_cable
from code.functions.lay_cables import create_cable
import copy
import random

def swap(district):

    # swapped = False
    old_cost = district.costs_shared

    #print(f"house: {house.id},  cheapest connection: {old_cost}")

    swap_district = copy.deepcopy(district)

    #list_available_houses = swap_capacity(copy_district, copy_house)


    for house in swap_district.houses:

        # print(f"Cables: {len(house.cables)}")
        random_house = random.choice(swap_district.houses)
        
        random_battery = random_house.connected_battery
        old_battery = house.connected_battery

        print(f"length house cables: {len(house.cables)}")
        print(f"length random house cables: {len(random_house.cables)}")

        # nieuwe lijst. hier komt in: alle elementen van alle kabels die op die batterij aangesloten zijn. MINUS kabels die in random_house.cables zitten.
        random_battery_cables = list(set(random_battery.cables).difference(random_house.cables))

        random_battery.cables = random_battery_cables
        random_house.cables = []

        for element in random_battery_cables:
            for cable in swap_district.cables_coordinates:
                if element == cable:
                    # print("deleting cable from district")
                    del cable
            # print("deleting cable from battery.")
            del element

        # print(f"random_battery_cables: {random_battery_cables}")
        old_battery_cables = list(set(old_battery.cables).difference(house.cables))

        old_battery.cables = old_battery_cables
        for element in old_battery_cables:
            del element
        
        house.cables = []


        # print(f"old battery: {house.connected_battery.id}")
        house.connected_battery = random_battery
        # print(f"New battery: {house.connected_battery.id}")
        random_house.connected_battery = old_battery

        closest_cable = find_closest_cable(random_battery, house)
        # print(f"House X: {house.x_coordinate} house Y: {house.y_coordinate}")
        # print(f"Closest cable= x: {closest_cable.x_coordinate}, Y: {closest_cable.y_coordinate}")
        new_cables = create_cable(house.x_coordinate, house.y_coordinate, closest_cable.x_coordinate, closest_cable.y_coordinate, swap_district, house, random_battery)
        swap_district.update_cost(len(new_cables), 9)
        # print(f"new cables: {house.cables}. {len(house.cables)}")
        closest_cable_2 = find_closest_cable(old_battery, random_house)
        new_cables = create_cable(random_house.x_coordinate, random_house.y_coordinate, closest_cable_2.x_coordinate, closest_cable_2.y_coordinate, swap_district, random_house, old_battery)
        swap_district.update_cost(len(new_cables), 9)


        new_cable_length1 = len(house.cables)
        new_cable_length2 = len(random_house.cables)
        print(f"length house new cables: {new_cable_length1}")
        print(f"length new house new cables: {new_cable_length2}")
        new_cost = swap_district.costs_shared

        if new_cost < old_cost:
            # print("over naar nieuw district")
            print(f"New Cost: {new_cost}")
            print(f"Old cost: {old_cost}")
            swapped = True
            old_cost = new_cost
            district = swap_district
        else:
            print("New cost is not less than old cost. ")
            swap_district = district

    return district
