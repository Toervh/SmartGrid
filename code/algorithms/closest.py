from code.functions.find_closest_node import find_closest_node
from code.functions.lay_cables import create_cable
from code.algorithms.hillclimber import Hillclimber
from code.functions.swap import swap
import copy

class Closest:
    """
    closest chooses the shortest distance
    between the current house and the batteries.
    Checks the capacity and calculates the distance.
    MAY CAUSE ENDLESS LOOP
    """

    def __init__(self, district):
        self.district = copy.deepcopy(district)
        # district.shuffle_houses()


    def closest_assignment(self, district):
        closest_district = None
        district.shuffle_houses()

        district.update_cost(len(district.batteries), 5000)
        for house in district.houses:

            # Call function to find the closest node to the house.
            closest_node = find_closest_node(district, house)
            # if closest_node is None:
            #     return False

            # Set closest x and y coordinates
            closest_x = closest_node.x_coordinate
            closest_y = closest_node.y_coordinate

            # create connection and all cables in between house and closest node.
            cables = create_cable(house.x_coordinate, house.y_coordinate, closest_x, closest_y, district, house, house.connected_battery)
            district.update_cost(len(cables), 9)
        # Return the connected district.
        closest_district = district


        return closest_district

    def run(self):
        initializing_district = self.district
        closest_district = self.closest_assignment(initializing_district)
        return closest_district