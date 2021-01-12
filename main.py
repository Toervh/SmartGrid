import csv
from code.classes.battery import Battery
from code.classes.house import House
from code.classes.district import District
from code.functions.readfile import load_battery_file, load_house_file
from code.algorithms.randomize import random_assignment
from code.functions.lay_cables import lay_cables
from visualise import visualise
from pprint import pprint
import matplotlib.pyplot as plt


if __name__ == '__main__':
    list_battery_objects = load_battery_file('data/Huizen&Batterijen/district_1/district-1_batteries.csv')
    list_house_objects = load_house_file('data/Huizen&Batterijen/district_1/district-1_houses.csv')

    id = 1
    d = District(id, list_house_objects, list_battery_objects)

    randomized_district = random_assignment(d)
    cabled_random_district = lay_cables(random_assignment)

    a = visualise(randomized_district)

