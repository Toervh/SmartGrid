import csv
from pprint import pprint
from code.classes.district import District
from code.algorithms.closest import closest_assignment
from code.algorithms.randomize import random_assignment


def run_multiple_random(list_house_objects, list_battery_objects):
    """
    Runs the randomizer multiple times. 
    Make sure to turn of the capacity checker in randomize.py 
    otherwise it will quit after an index error. Returns the average score
    and the list of results.
    """

    i = 0
    cost_sum = 0
    list_cost = []
    while i < 100:
        r = District(id, list_house_objects, list_battery_objects)
        randomized_district = random_assignment(r)
        cost_sum+=randomized_district.costs_shared
        list_cost.append(randomized_district.costs_shared)
        i+=1
        print(f"Cost shared: {randomized_district.costs_shared}")
    cost_average = cost_sum/100
    return print(cost_average, list_cost)


def run_multiple_closest(district):
    """
    Runs closest.py multiple times. 
    Make sure to change the list to picking a random house to start 
    with in closest.py. Returns the average score and the list of results.
    """
    i = 0
    cost_sum = 0
    list_cost = []
    while i < 100:
        closest_district = closest_assignment(district)
        cost_sum+=closest_district.costs_shared
        list_cost.append(closest_district.costs_shared)
        i+=1
        print(f"Cost shared: {closest_district.costs_shared}")
    cost_average = cost_sum/100
    return print(cost_average)
