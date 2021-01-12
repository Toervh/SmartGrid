import csv
from code.classes.battery import Battery
from code.classes.house import House
from code.classes.district import District
from code.functions.readfile import load_battery_file, load_house_file
from code.algorithms.randomize import random_assignment
from code.algorithms.closest import closest_assignment
from code.classes.cable import Cable
from code.functions.visualise import visualise
from pprint import pprint
import matplotlib.pyplot as plt


def run_multiple_random(list_house_objects, list_battery_objects):
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
    i = 0
    cost_sum = 0
    while i < 5:
        closest_district = closest_assignment(district)
        cost_sum+=closest_district.costs_shared
        i+=1
    cost_average = cost_sum/100
    return print(cost_average)
