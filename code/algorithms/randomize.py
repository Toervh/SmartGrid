import random
from code.classes.cable import Cable
import copy

def random_assignment(district):
    """
    Randomly assign each node with one of the possibilities.
    """
    non_random_district = district

    # Loops through all the hosues
    for house in non_random_district.houses:
        list_available_batteries = []
        # print(f"house output: {house.output}")

        # Checks if the battery can handle the house output
        for battery in district.batteries:
            if battery.check_capacity(house.output):
                list_available_batteries.append(battery)

        # print(f"available batteries: {list_available_batteries}")

        # Chooses a battery and connects it to the house currently on the loop
        random_battery = random.choice(list_available_batteries)

        # Adds house to battery
        house.add_connected_battery(random_battery.id)
        random_battery.add_houses(house.id)
        random_battery.add_houses_objects(house)
        random_battery.update_capacity(house.output)

        # Creates a cable to calculate the length.
        cable = Cable(house.x_coordinate, house.y_coordinate, random_battery.x_coordinate, random_battery.y_coordinate, non_random_district, house, random_battery)

    random_district = non_random_district

    return random_district