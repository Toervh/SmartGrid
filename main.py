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
import matplotlib.pyplot as plot
from multiple_average import run_multiple_random, run_multiple_closest

if __name__ == '__main__':
    list_battery_objects = load_battery_file('data/Huizen&Batterijen/district_1/district-1_batteries.csv')
    list_house_objects = load_house_file('data/Huizen&Batterijen/district_1/district-1_houses.csv')

    id = 1
    d = District(id, list_house_objects, list_battery_objects)

    closest_district = closest_assignment(d)
    a = visualise(closest_district)
    print(f"Cost shared: {closest_district.costs_shared}")

    # randomized_district = random_assignment(d)
    # a = visualise(randomized_district)
    # print(f"Cost shared: {randomized_district.costs_shared}")


    # average calculator
    # cost_sum = 0
    # i = 0
    # list_costs = []
    # while i < 100:
    #     r = District(id, list_house_objects, list_battery_objects)
    #     randomized_district = random_assignment(r)
    #     cost_sum+=randomized_district.costs_shared
    #     i+=1
    #     list_costs.append(randomized_district.costs_shared)
    #     print(f"Cost shared: {randomized_district.costs_shared}")

    # print(list_costs)
    # cost_average = cost_sum/100
    # print(cost_sum)
    # print(cost_average)

    # multiple_random = run_multiple_random(d)

    # multiple_closest = run_multiple_closest(d)
