import csv
from code.classes.battery import Battery
from code.classes.house import House
from code.classes.district import District
from code.functions.readfile import load_battery_file, load_house_file
from code.algorithms.randomize import random_assignment
from code.algorithms.closest import closest_assignment
from code.functions.lay_cables import create_cable
from code.classes.cable import Cable
from code.functions.visualise import visualise
from pprint import pprint
import matplotlib.pyplot as plot
from code.functions.multiple_average import run_multiple_random, run_multiple_closest
from code.functions.prompts import choose_algorithm, choose_district

if __name__ == '__main__':
    district_chosen = choose_district()
    instance = choose_algorithm(district_chosen[1], district_chosen[0])
    visualise(instance)

    # caymins clustering
    # a* op batterij
    #