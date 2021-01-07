import random
import copy




def random_assignment(district, batteries):
    """
    Randomly assign each node with one of the possibilities.
    """
    for house in district.houses:
        house.add_connected_battery(random.choice(batteries))