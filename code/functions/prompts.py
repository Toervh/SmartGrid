import csv
import copy
from code.classes.district import District
from code.functions.readfile import load_battery_file, load_house_file
from code.algorithms.randomize import Random
from code.algorithms.closest import Closest
from code.classes.exceptions import NoBatteryError
from code.functions.visualise import visualise
from pprint import pprint
from code.functions.multiple_average import run_multiple_random, run_multiple_closest

def choose_algorithm(list_house_objects, list_battery_objects):
    id = 1
    d = District(id, list_house_objects, list_battery_objects)
    d.shuffle_houses()

    keynames = ["random", "closest", "multiple random", "multiple closest"]

    print('What algorithm do you want to run?')
    print('==========')
    print(' Random\n Closest\n Multiple Random\n Multiple Closest')
    print('==========')

    while True:
        program = input('Choice: ')
        lower_program = program.lower()
        if lower_program in keynames:
            break
        print('Algorithm not found, try again.')

    if program == 'multiple random':
        with open("results_random.txt", "a") as file_results:
            for num in range(1000):
                try:
                    original_district = copy.deepcopy(d)
                    initializing_district = Random(original_district)
                    random_district = initializing_district.run()
                    file_results.write(f"try: {num}. Result:" )
                    file_results.write(str(random_district.costs_shared) + '\n')
                except NoBatteryError:
                    pass
            print(sorted(results_list))
    elif program == 'closest':
        while True:
            try:
                original_district = copy.deepcopy(d)
                initializing_district = Closest(original_district)
                closest_district = initializing_district.run()
                break

            except NoBatteryError:
                pass

        a = visualise(closest_district)
        closest_district.dict_me()
        print(f"Cost shared: {closest_district.costs_shared}")
        return closest_district
    elif program == 'multiple closest':
        print("You selected multiple closest.")        
        with open("results.txt", "a") as file_results:
            results_list = []
            for num in range(10000):
        
                try:
                    original_district = copy.deepcopy(d)
                    initializing_district = Closest(original_district)
                    closest_district = initializing_district.run()
                    file_results.write(f"try: {num}. Result:" )
                    file_results.write(str(closest_district.costs_shared) + '\n')
                    results_list.append(closest_district.costs_shared)

                except NoBatteryError:
                    pass
            print(results_list)

            sum_list = sum(results_list)
            average = sum_list/len(results_list)

            file_results.write("Average: ")
            file_results.write(str(average) + '\n')
            sort_list = sorted(results_list)
            lowest = sort_list[0]
            print(lowest)

    elif program == 'random':
        print("You selected random.")
        while True:
            try:
                original_district = copy.deepcopy(d)
                initializing_district = Random(original_district)
                randomized_district = initializing_district.run()

                break
            except NoBatteryError:
                pass
        randomized_district.dict_me()
        a = visualise(randomized_district)
        print(f"Cost shared: {randomized_district.costs_shared}")

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
