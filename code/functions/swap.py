from code.functions.find_closest_cable import find_closest_cable
from code.functions.lay_cables import create_cable
import copy
import random

def swap(district):

    old_cost = district.costs_shared

    swap_district = copy.deepcopy(district)

    for house in swap_district.houses:
        list_swapped_districts = []

        for other_house in swap_district.houses:

            # Store their old battery objects here.
            old_battery1 = house.connected_battery
            old_battery2 = other_house.connected_battery

            # Checking available capacity.
            available_capacity1 = old_battery1.capacity - (old_battery1.current_capacity - house.output)
            if other_house.output > available_capacity1:
                break
            available_capacity2 = old_battery2.capacity - (old_battery2.current_capacity - other_house.output)
            if house.output > available_capacity2:
                break

            # Store the list of objects of their old cables here.
            old_cables1 = house.cables
            old_cables2 = other_house.cables

            # Reset their list of cables.
            house.cables = []
            other_house.cables = []

            # decrease cost of district by length of both old cables
            swap_district.degrade_cost(len(old_cables1) + len(old_cables2), 9)


            # Deleting cable Objects from both District and their respective batteries.
            for element in old_cables1:
                if element in swap_district.cable_objects:
                    swap_district.cable_objects.remove(element)

            for element in old_cables1:
                if element in old_battery1.cables:
                    old_battery1.cables.remove(element)

            for element in old_cables2:
                if element in swap_district.cable_objects:
                    swap_district.cable_objects.remove(element)

            for element in old_cables2:
                if element in old_battery2.cables:
                    old_battery2.cables.remove(element)

            # Reset both houses cables
            house.cables = []
            other_house.cables = []

            # Reconnect their batteries with each other.
            house.connected_battery = old_battery2
            other_house.connected_battery = old_battery1

            # For the first house, find the closest cable to his new battery
            closest_cable = find_closest_cable(old_battery2, house)
            # Create cables between first house and his new battery
            new_cables = create_cable(house.x_coordinate, house.y_coordinate, closest_cable.x_coordinate, closest_cable.y_coordinate, swap_district, house, old_battery2)
            # Update the cost for that connection.
            swap_district.update_cost(len(new_cables), 9)

            # For the second house, find the closest cable to his new battery
            closest_cable_2 = find_closest_cable(old_battery1, other_house)
            # Create cables between second house and his new battery
            new_cables = create_cable(other_house.x_coordinate, other_house.y_coordinate, closest_cable_2.x_coordinate, closest_cable_2.y_coordinate, swap_district, other_house, old_battery1)
            # Update the cost for that connection.
            swap_district.update_cost(len(new_cables), 9)

            # Set new districts cost to new_cost
            new_cost = swap_district.costs_shared

            # Compare this cost to the original state. If it is an improvement, add it to the list of possibilities.
            if new_cost < old_cost:
                old_cost = new_cost
                list_swapped_districts.append(swap_district)
            else:
                pass

        cheapest = district.costs_shared
        for swapped_district in list_swapped_districts:
            if swapped_district.costs_shared > cheapest:
                district = swapped_district
    return district
