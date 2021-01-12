import random
import copy

def random_assignment(district):
    """
    Randomly assign each node with one of the possibilities.
    """
    non_random_district = district

    for house in non_random_district.houses:
        list_available_batteries = []
        print(f"house output: {house.output}")

        for battery in district.batteries:
            if battery.check_capacity(house.output):
                list_available_batteries.append(battery)

        print(f"available batteries: {list_available_batteries}")
        random_battery = random.choice(list_available_batteries)

        house.add_connected_battery(random_battery.id)
        random_battery.add_houses(house.id)
        random_battery.add_houses_objects(house)
        random_battery.update_capacity(house.output)


    random_district = non_random_district

    return random_district