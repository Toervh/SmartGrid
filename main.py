import csv
import copy
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
from pprint import pprint
import matplotlib.pyplot as plot
from code.functions.multiple_average import run_multiple_random, run_multiple_closest
from code.functions.prompts import choose_algorithm, choose_district

if __name__ == '__main__':
    district_chosen = choose_district()
    instance = choose_algorithm(district_chosen[1], district_chosen[0])
    visualise(instance)

    #Instantiating the object.
    d = District(id, list_house_objects, list_battery_objects)

    # ****-------------SHUFFLE HOUSES FOR RANDOM RESULT-------------****
    # d.shuffle_houses()

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


    # ****------------------RUNS CLOSEST DISTRICT--------------------****
    # while True:
    #     try:
    #         original_district = copy.deepcopy(d)
    #         closest_district = closest_assignment(original_district)
    #         break
    #
    #     except NoBatteryError:
    #         pass
    #
    # a = visualise(closest_district)
    # closest_district.dict_me()
    # print(f"Cost shared: {closest_district.costs_shared}")


    # ****------------------RUNS RANDOM DISTRICT---------------------****
    while True:
        try:
            original_district = copy.deepcopy(d)
            randomized_district = random_assignment(original_district)

            break

        except NoBatteryError:
            pass
    randomized_district.dict_me()
    a = visualise(randomized_district)
    print(f"Cost shared: {randomized_district.costs_shared}")

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


