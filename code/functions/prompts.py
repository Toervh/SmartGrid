import csv
import copy
from code.classes.district import District
from code.functions.readfile import load_battery_file, load_house_file
from code.algorithms.randomize import random_assignment
from code.algorithms.closest import closest_assignment
from code.classes.exceptions import NoBatteryError
from code.functions.visualise import visualise
from pprint import pprint
from code.functions.multiple_average import run_multiple_random, run_multiple_closest

def choose_algorithm(list_house_objects, list_battery_objects):
    id = 1
    d = District(id, list_house_objects, list_battery_objects)
    d.shuffle_houses()

    keynames = ["random", "closest", "multiple_random", "multiple_random_closest"]

    print('What algorithm do you want to run?')
    print('==========')
    print(' Random\n Closest\n Multiple Random\n Multiple Randomized Closest')
    print('==========')

    while True:
        program = input('Choice: ')
        lower_program = program.lower()
        if lower_program in keynames:
            break
        print('Algorithm not found, try again.')

    if program == 'multiple_random':
        return run_multiple_random(list_house_objects, list_battery_objects)
    elif program == 'closest':
        while True:
            try:
                original_district = copy.deepcopy(d)
                closest_district = closest_assignment(original_district)
                break

            except NoBatteryError:
                pass

        a = visualise(closest_district)
        # closest_district.dict_me()
        print(f"Cost shared: {closest_district.costs_shared}")
        return closest_district
    elif program == 'multiple_random_closest':
        return run_multiple_closest
    elif program == 'random':
        return random_assignment(d)

def choose_district():
    district_dict = {
        '1': 'data/Huizen&Batterijen/district_1/district-1_',
        '2': 'data/Huizen&Batterijen/district_2/district-2_',
        '3': 'data/Huizen&Batterijen/district_3/district-3_'
    }
    print('Welcome to SmartGrid algorithms')
    print('==========')
    while True:
        what_district = input('What district do you want to run?\nChoices are: 1, 2, 3\n')
        if what_district in district_dict.keys():
            break
        print('Retry please.')
    battery_csv = 'batteries.csv'
    houses_csv = 'houses.csv'

    battery_file = district_dict[what_district] + battery_csv
    houses_file = district_dict[what_district] + houses_csv

    #Hardcoded only district 1, can change it by changing the files
    list_all_objects = []
    list_battery_objects = load_battery_file(battery_file)
    list_house_objects = load_house_file(houses_file)
    list_all_objects.append(list_battery_objects)
    list_all_objects.append(list_house_objects)
    print(f"Loaded District {what_district}.\n\n")
    return list_all_objects
