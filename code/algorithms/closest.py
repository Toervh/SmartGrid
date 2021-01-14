from code.functions.find_closest_node import find_closest_node
from code.functions.lay_cables import create_cable

def closest_assignment(district):
    """
    closest chooses the shortest distance
    between the current house and the batteries.
    Checks the capacity and calculates the distance.
    """

    for house in district.houses:

        # Call function to find the closest node to the house.
        closest_node = find_closest_node(district, house)

        # Set closest x and y coordinates
        closest_x = closest_node.x_coordinate
        closest_y = closest_node.y_coordinate

        # create connection and all cables in between house and closest node.
        create_cable(house.x_coordinate, house.y_coordinate, closest_x, closest_y, district, house, house.connected_battery)

    # Return the connected district.
    closest_district = district

    return closest_district