import random
from code.classes.cable import Cable
from code.functions.lay_cables import create_cable
from code.functions.find_closest_cable import find_closest_cable
import copy

def random_assignment(district):
    """
    Randomly assign each node with one of the possibilities.
    """

    random_district = None

    # Loops through all the houses
    for house in district.houses:

        list_available_batteries = []

        # Checks if the battery can handle the house output
        for battery in district.batteries:

            if battery.check_capacity(house.output):
                list_available_batteries.append(battery)
                # print(f"battery: {battery.id} is at: {battery.current_capacity}")
            # else:
            #     print(f"battery: {battery.id} is at maximum capacity")

        # Chooses a battery and connects it to the house currently on the loop
        random_battery = random.choice(list_available_batteries)


        # Set closest x and y coordinates of that battery
        closest_node = find_closest_cable(random_battery, house)

        closest_x = closest_node.x_coordinate
        closest_y = closest_node.y_coordinate

        # Adds house to battery
        house.add_connected_battery(random_battery)
        random_battery.add_houses(house.id)
        random_battery.add_houses_objects(house)
        random_battery.update_capacity(house.output)

    # Creates a cable to calculate the length.
    create_cable(house.x_coordinate, house.y_coordinate, closest_x, closest_y, non_random_district, house,
                 random_battery)

    random_district = non_random_district



    return random_district