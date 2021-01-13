from code.functions.find_closest_node import find_closest_node
from code.functions.lay_cables import create_cable

def new_closest_assignment(district):

    district.shuffle_houses()
    for house in district.houses:

        closest_node = find_closest_node(district, house)

        closest_x = closest_node.x_coordinate
        closest_y = closest_node.y_coordinate


        create_cable(house.x_coordinate, house.y_coordinate, closest_x, closest_y, district, house, house.connected_battery)

    closest_district = district

    return closest_district