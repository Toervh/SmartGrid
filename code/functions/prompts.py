import csv
import copy
from code.classes.district import District
from code.functions.readfile import load_battery_file, load_house_file
from code.algorithms.randomize import Random
from code.algorithms.hillclimber import Hillclimber
from code.algorithms.closest import Closest
from code.algorithms.kmeans import K_means
from code.classes.exceptions import NoBatteryError
from code.functions.results_graph import plot_results
from code.functions.visualise import visualise
from code.functions.swap import swap
from pprint import pprint

def choose_algorithm(list_house_objects, list_battery_objects):
    id = 1
    d = District(id, list_house_objects, list_battery_objects)
    # d.shuffle_houses()

    keynames = ["random", "closest", "multiple random", "multiple closest", "k-means"]

    print('What algorithm do you want to run?')
    print('==========')
    print(' Random\n Closest\n Multiple Random\n Multiple Closest\n K-Means')
    print('==========')

    while True:
        program = input('Choice: ')
        lower_program = program.lower()
        if lower_program in keynames:
            break
        print('Algorithm not found, try again.')

    if program == 'multiple random':
        N = input("You selected multiple random. How many?")
        int_n = int(N)
        with open("results_random.txt", "a") as file_results:
            for num in range(int_n):
                try:
                    original_district = copy.deepcopy(d)
                    random_district = Random(original_district)
                    finished_district = random_district.run()
                    file_results.write(f"try: {num}. Result:" )
                    file_results.write(str(finished_district.costs_shared) + '\n')
                except NoBatteryError:
                    pass
            print(sorted(results_list))

    # CLOSEST
    elif program == 'closest':
        while True:
            try:
                original_district = copy.deepcopy(d)
                initializing_district = Closest(original_district)
                finished_district = initializing_district.run()
                break

            except NoBatteryError:
                pass

        climber_district = Hillclimber(finished_district)
        c_district = climber_district.district
        a = visualise(c_district)
        finished_district.dict_me()
        print(f"Cost shared: {finished_district.costs_shared}")
        return finished_district



    elif program == 'multiple closest':
        N = input("You selected multiple closest. How many?")       
        int_n = int(N)
        results_list = []
        with open("results.txt", "a") as file_results:
            results_list = []
            for num in range(int_n):
        
                try:
                    original_district = copy.deepcopy(d)
                    initializing_district = Closest(original_district)
                    closest_district = initializing_district.run()
                    results_list.append(closest_district)
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

    elif program == 'k-means':
        print("You selected K-means.")
        list_results = []
        list_districts = []
        i = 0
        while len(list_results) < 100:
            while True:
                try:
                    original_district = copy.deepcopy(d)
                    initializing_district = K_means(original_district)
                    k_means_district = initializing_district.run()
                    list_results.append(k_means_district.costs_shared)
                    list_districts.append(k_means_district)
                    break

                except NoBatteryError:
                    pass
            i += 1
            print(i)
        plot_results(list_results)
        j = 0
        lowest_cost = 50000
        lowest_cost_district = None
        for j in range(len(list_results)):
            if list_results[j] < lowest_cost:
                lowest_cost = list_results[j]
                lowest_cost_district = list_districts[j]
            j += 1
        print(sum(list_results) / len(list_results))
        print(lowest_cost_district.costs_shared)
        a = visualise(lowest_cost_district)

    # if program == 'closest' or 'random' or 'k-means':
    #         while True:
    #             hillclimber_input = input('Do you want to optimize using Hillclimber? Y/N')
    #             if hillclimber_input.tolower() == 'y':
    #                 break
    #             elif hillclimber_input.tolower() == 'n':
    #                 print('Goodbye.')
    #                 quit()

    #             print('Not the right input.')
    #         #climber_district = Hillclimber(finished_district)
    #         #climber_district.run()
    # elif program == 'multiple closest' or 'multiple random':
    #     while True:
    #         hillclimber_input = input('Do you want to optimize the cheapest district using Hillclimber? Y/N')
    #         if hillclimber_input.tolower() == 'y':
    #             break
    #         elif hillclimber_input.tolower() == 'n':
    #             print('Goodbye.')
    #             quit()

    #         print('Not the right input.')

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
