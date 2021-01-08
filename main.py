import csv
from code.classes.battery import Battery
from code.classes.house import House
from code.classes.district import District
from code.functions.readfile import load_battery_file, load_house_file
from code.functions.jsonify import json_output
from code.algorithms.randomize import random_assignment
from code.functions.printdistrict import print_district
from pprint import pprint
import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':
    list_battery_objects = load_battery_file('data/Huizen&Batterijen/district_1/district-1_batteries.csv')
    list_house_objects = load_house_file('data/Huizen&Batterijen/district_1/district-1_houses.csv')

    d = District(list_house_objects, list_battery_objects)
    print_district(d)
    # pprint(vars(d))
    randomized_district = random_assignment(d)
    print_district(randomized_district)
    b = Battery()
    print(b.__dict__)
