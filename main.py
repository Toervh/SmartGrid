import csv
from code.classes.battery import Battery
from code.classes.house import House
from code.classes.district import District
from code.functions.readfile import load_battery_file, load_house_file
from code.algorithms.randomize import random_assignment
from code.algorithms.closest import closest_assignment
from code.algorithms.new_closest import new_closest_assignment
from code.classes.cable import Cable
from code.functions.visualise import visualise
from pprint import pprint
import matplotlib.pyplot as plot
from code.functions.multiple_average import run_multiple_random, run_multiple_closest

if __name__ == '__main__':
    list_battery_objects = load_battery_file('data/Huizen&Batterijen/district_1/district-1_batteries.csv')
    list_house_objects = load_house_file('data/Huizen&Batterijen/district_1/district-1_houses.csv')

    id = 1
    d = District(id, list_house_objects, list_battery_objects)

    closest_district = new_closest_assignment(d)
    a = visualise(closest_district)
    print(f"Cost shared: {closest_district.costs_shared}")

    # randomized_district = random_assignment(d)
    # a = visualise(randomized_district)
    # print(f"Cost shared: {randomized_district.costs_shared}")

    # run_multiple_random(list_house_objects, list_battery_objects)

    # multiple_closest = run_multiple_closest(d)


    # battery1 = closest_district.batteries[0]
    # for i in battery1.cables:
    #     print(f"{i}")
    # print(f"battery: {battery1.id}, cable 0: {battery1.cables[0]}")
    # house1 = closest_district.houses[0]
    # print(f"house: {house1.id}, cables: {house1.cables}")