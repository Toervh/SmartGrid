from code.functions.find_closest_node import find_closest_node
from code.functions.lay_cables import create_cable
from code.functions.swap import swap

def closest_assignment(district):
    """
    closest chooses the shortest distance
    between the current house and the batteries.
    Checks the capacity and calculates the distance.
    MAY CAUSE ENDLESS LOOP
    """
    closest_district = None
    district.shuffle_houses()

    for house in district.houses:

        # Call function to find the closest node to the house.
        closest_node = find_closest_node(district, house)
        # if closest_node is None:
        #     return False

        # Set closest x and y coordinates
        closest_x = closest_node.x_coordinate
        closest_y = closest_node.y_coordinate

        # create connection and all cables in between house and closest node.
        create_cable(house.x_coordinate, house.y_coordinate, closest_x, closest_y, district, house, house.connected_battery)

    # Return the connected district.
    closest_district = district


    closest_district.shuffle_houses()
    climber_district = swap(closest_district)
    # for battery in closest_district.batteries:
    #     for house in battery.houses_objects:
    #         print(f"{house}")
    #         print(f"old battery = {house.connected_battery.id}")
    #         house_swap = swap(closest_district)
    #         if house_swap:

    #             print(f"house: {house.id} swapped. new battery: {house.connected_battery.id}")
    #         # if house_swap:
    #         #     closest_assignment(closest_district)
    #     for battery in closest_district.batteries:
    #         print(f"battery {battery.id}. capacity: {battery.current_capacity}")
    return climber_district