from code.functions.find_closest_node import find_closest_node
from code.functions.lay_cables import create_cable
from code.classes.district import District
from code.functions.find_closest_cable import find_closest_cable
import copy

class Hillclimber:
    """
    Hill Climber takes a already connected district and optimizes the connections.
    It does so by iterating taking every house and comparing it with every other house so see if :
    1: they can fit on each others battery. If not it passes to the next house for comparison.
    2: if it fits it checks if the connection the houses have now is cheaper than the connection they would have with each others battery.
    3: if the connection they would have if they swapped was cheaper, it swaps the connections.
    hillclimber saves the swapped state in a list, from which we will grab the best state at the end of the comparison.
    After all houses have been compared to all houses it returns the optimized state to the user.
    """
    def __init__(self, district):
        self.district = copy.deepcopy(district)

    def hillclimber(self, district):

        # Set the old cost for comparison
        old_cost = district.costs_shared

        # Deepcopy. Not sure if necessary.
        swap_district = copy.deepcopy(district)

        # Iterate over every house in the district.
        for house in swap_district.houses:

            # Make a list which will be filled with states in which this house is swapped with another.
            # At the end of iterating over all other houses we will pick the best state.
            list_swapped_districts = []

            # Loop over all other houses to start comparison.
            for other_house in swap_district.houses:

                # Store their old battery objects here.
                old_battery1 = house.connected_battery
                old_battery2 = other_house.connected_battery

                # Checking available capacity. If not possible: Break from this loop and go to next battery.
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
                new_cables = create_cable(house.x_coordinate, house.y_coordinate, closest_cable.x_coordinate,
                                          closest_cable.y_coordinate, swap_district, house, old_battery2)
                # Update the cost for that connection.
                swap_district.update_cost(len(new_cables), 9)

                # For the second house, find the closest cable to his new battery
                closest_cable_2 = find_closest_cable(old_battery1, other_house)
                # Create cables between second house and his new battery
                new_cables = create_cable(other_house.x_coordinate, other_house.y_coordinate,
                                          closest_cable_2.x_coordinate, closest_cable_2.y_coordinate, swap_district,
                                          other_house, old_battery1)
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

            # Current district is the cheapest district.
            cheapest = district.costs_shared

            # Check all districts to see if they are cheaper than the original district.
            # If so make that district into the cheapest.
            for swapped_district in list_swapped_districts:
                if swapped_district.costs_shared > cheapest:
                    district = swapped_district

        return district

    def run(self):
        initializing_district = self.district
        hillclimber_district = self.hillclimber(initializing_district)
        print(hillclimber_district)
        return hillclimber_district