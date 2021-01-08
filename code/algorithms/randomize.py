import random
import copy




def random_assignment(district):
    """
    Randomly assign each node with one of the possibilities.
    """
    non_random_district = district
    for house in non_random_district.houses:
        random_battery = random.choice(district.batteries)
        house.add_connected_battery(random_battery.id)
        random_battery.add_houses(house.id)
        random_battery.add_houses_objects(house)

    return non_random_district