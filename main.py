import csv
import copy
import time
from datetime import timedelta
from code.classes.battery import Battery
from code.classes.house import House
from code.classes.district import District
from code.functions.readfile import load_battery_file, load_house_file
from code.algorithms.randomize import random_assignment
from code.algorithms.closest import closest_assignment
from code.functions.lay_cables import create_cable
from code.classes.cable import Cable
from code.functions.visualise import visualise
from code.classes.exceptions import NoBatteryError
from code.algorithms.kmeans import k_means
from code.functions.results_graph import plot_results
from code.functions.swap import swap
from pprint import pprint
import matplotlib.pyplot as plot
from code.functions.multiple_average import run_multiple_random, run_multiple_closest
from code.functions.prompts import choose_algorithm, choose_district


if __name__ == '__main__':

    # ****-------------Instantiating the object-------------****
    district_chosen = choose_district()
    d = District(id, district_chosen[1], district_chosen[0])
    # choose_algorithm(district_chosen[1], district_chosen[0])
    # ****-------------SHUFFLE HOUSES FOR RANDOM RESULT-------------****
    # d.shuffle_houses()
    # start_time = time.monotonic()
    # end_time = time.monotonic()
    # print(timedelta(seconds=end_time - start_time))
    # print('Welcome to SmartGrid algorithms')
    # print('==========')
    # print(' Random\n Closest\n Multiple Random\n Multiple Randomized Closest')
    # print('==========')
    # program = input('What program would you like to run?\n' )
    #
    # prompting_dict = {
    #     'Random': random_assignment(d),
    #     'Closest': closest_assignment(d),
    #     'Multiple Random': run_multiple_random(list_house_objects, list_battery_objects),
    #     'Multiple Randomized Closest': run_multiple_closest(d)
    # }

    # run = prompting_dict[program]
    #
    #
    # def can_cause_index_error(some_list):
    #     other_list = []
    #     for element in some_list:
    #         if element not in taken_list:
    #             other_list.append(element)
    #
    #     raise Exception("no options"):
    #
    #     return other_list
    # option = [1, 2, 3, 4]
    #
    # while True:
    #     options = can_cause_index_error(option)
    #
    #     taken_list.append

    # ****------------------RUNS K-MEANS ClUSTERING DISTRICT--------------------****
    list_results = []
    list_districts = []
    i = 0
    while len(list_results) < 10:
        while True:
            try:
                original_district = copy.deepcopy(d)
                k_means_district = k_means(original_district)
                list_results.append(k_means_district.costs_shared)
                list_districts.append(k_means_district)
                visualise(k_means_district)
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
    visualise(lowest_cost_district)
    # ****------------------RUNS CLOSEST DISTRICT--------------------****
    # list_results = []
    # list_districts = []
    # while len(list_results) < 1:
    #     while True:
    #         try:
    #             original_district = copy.deepcopy(d)
    #             closest_district = closest_assignment(original_district)
    #             list_results.append(closest_district.costs_shared)
    #             print("One iteration done")
    #             print(closest_district.costs_shared)
    #             a = visualise(closest_district)
    #             break
    #
    #         except NoBatteryError:
    #             pass
    #
    # # a = visualise(closest_district)
    # closest_district.dict_me()
    # print(f"Cost shared: {closest_district.costs_shared}")
    #
    # plot_results(list_results)

    # ****------------------RUNS RANDOM DISTRICT---------------------****
    # while True:
    #     try:
    #         original_district = copy.deepcopy(d)
    #         randomized_district = random_assignment(original_district)
    #
    #         break
    #
    #     except NoBatteryError:
    #         pass
    # randomized_district.dict_me()
    # a = visualise(randomized_district)
    # print(f"Cost shared: {randomized_district.costs_shared}")

    # ****------------------RUNS MULTIPLE RANDOM---------------------****
    # run_multiple_random(list_house_objects, list_battery_objects)
    # run_multiple_random(list_house_objects, list_battery_objects)



    # ****------------------RUNS MULTIPLE RANDOMIZED CLOSEST---------****
    # multiple_closest = run_multiple_closest(d)
    # with open("results.txt", "a") as file_results:
    #
    #     for num in range(100):
    #
    #         try:
    #             original_district = copy.deepcopy(d)
    #             closest_district = closest_assignment(original_district)
    #             file_results.write(f"try: {num}. Result:" )
    #             file_results.write(str(closest_district.costs_shared) + '\n')
    #
    #
    #         except NoBatteryError:
    #             pass


