import csv
import copy
from code.classes.district import District
from code.algorithms.randomize import Random
from code.algorithms.hillclimber import Hillclimber
from code.algorithms.closest import Closest
from code.algorithms.kmeans import K_means
from code.classes.exceptions import NoBatteryError
from code.classes.battery import Battery
from code.classes.house import House
from code.algorithms.visualise import visualise
from code.functions.results_graph import plot_results
from code.functions.swap import swap
from pprint import pprint

class Prompt:
    """Prompt is an empty class to instantiate the program."""
    pass

    def choose_algorithm(self, list_house_objects, list_battery_objects):
        """prints frontend and executes the algorithm based on the choice, saves the results and visualises it"""

        # Initializing district object
        id = 1
        d = District(id, list_house_objects, list_battery_objects)

        keynames = ["random", "closest", "multiple random", "multiple closest", "k-means"]
        
        # Frontend
        print('What algorithm do you want to run?')
        print('==========')
        print(' Random\n Closest\n Multiple Random\n Multiple Closest\n K-Means')
        print('==========')

        # Will take input from user and crossreference with list of algorithms.
        while True:
            program = input('Choice: ')
            lower_program = program.lower()
            if lower_program in keynames:
                break
            print('Algorithm not found, try again.')

        # Execution of code requested of user.
        if program == 'multiple random':

            # Asking of x times running the code and initializing of analysis
            N = input("You selected multiple random. How many?")
            int_n = int(N)
            results_list = []
            
            # Code will write results to a txt file
            with open("results_random.txt", "a") as file_results:
                cost_shared_list = []
                for num in range(int_n):
                    
                    try:
                    # Try will only find valid solutions
                        original_district = copy.deepcopy(d)
                        random_district = Random(original_district)
                        finished_district = random_district.run()

                        # Writer
                        file_results.write(f"try: {num}. Result:" )
                        file_results.write(str(finished_district.costs_shared) + '\n')
                        
                        # Appends list so we can take the cheapest and perform operations on it (Hillclimber/Visualise)
                        results_list.append(finished_district)
                        cost_shared_list.append(finished_district.costs_shared)

                    except NoBatteryError:
                        pass
            
                # Making a list of tuples so we can sort it on it's cost shared value in descending order
                district_list = []
                for district in results_list:
                    district_list.append((district, district.costs_shared))
                
                # Picking the cheapest solution
                district_list.sort(key=lambda x:x[1])
                cheapest_tuple = district_list[0]
                cheapest_district = cheapest_tuple[0]

                # Output on terminal
                print(f"Cheapest district: {cheapest_district}, costs shared: {cheapest_district.costs_shared}")
                cheapest_district.dict_me()

                # Output in .txt file
                sum_list = sum(cost_shared_list)
                average = sum_list/len(cost_shared_list)
                file_results.write("Average: ")
                file_results.write(str(average) + '\n')
                self.choose_climber(cheapest_district)

        elif program == 'closest':
            while True:
                try:
                    # Try will only find valid solutions
                    original_district = copy.deepcopy(d)
                    closest_district = Closest(original_district)
                    finished_district = closest_district.run()
                    break

                except NoBatteryError:
                    pass

            # Output
            finished_district.dict_me()
            print(f"Cost shared: {finished_district.costs_shared}")
            self.choose_climber(finished_district)

        elif program == 'multiple closest':

            # Asking of x times running the code and initializing of analysis
            N = input("You selected multiple closest. How many?")       
            int_n = int(N)
            results_list = [] 

            # Code will write results to a txt file
            with open("results.txt", "a") as file_results:
                cost_shared_list = []
                for num in range(int_n):
            
                    try:
                    # Try ensures program does not crash if there is no valid solution found, will retry if so
                        original_district = copy.deepcopy(d)
                        initializing_district = Closest(original_district)
                        finished_district = initializing_district.run()

                        # Writer
                        cost_shared_list.append(finished_district.costs_shared)
                        file_results.write(f"try: {num}. Result:" )
                        file_results.write(str(finished_district.costs_shared) + '\n')

                        # Appends list so we can take the cheapest and perform operations on it (Hillclimber/Visualise)
                        results_list.append(finished_district)
                        cost_shared_list.append(finished_district.costs_shared)

                    except NoBatteryError:
                        pass

                # Making a list of tuples so we can sort it on it's cost shared value in descending order
                district_list = []
                for district in results_list:
                    district_list.append((district, district.costs_shared))

                # Picking the cheapest solution
                district_list.sort(key=lambda x:x[1])
                cheapest_tuple = district_list[0]
                cheapest_district = cheapest_tuple[0]

                # Output on terminal
                print(f"Cheapest district: {cheapest_district}, costs shared: {cheapest_district.costs_shared}")
                cheapest_district.dict_me()

                sum_list = sum(cost_shared_list)
                average = sum_list/len(cost_shared_list)

                # Output in .txt file
                file_results.write("Average: ")
                file_results.write(str(average) + '\n')

                # Next step
                self.choose_climber(cheapest_district)

        elif program == 'random':
            print("You selected random.")
            while True:                
                try:
                # Try will only find valid solutions
                    original_district = copy.deepcopy(d)
                    initializing_district = Random(original_district)
                    finished_district = initializing_district.run()
                    break
                except NoBatteryError:
                    pass
            print(f"Costs shared: {finished_district.costs_shared}")
            self.choose_climber(finished_district)
        
        elif program == 'k-means':

            N = input("You selected K-means. How many times?")
            int_n = int(N)
            list_results = []
            list_districts = []
            
            for num in range(int_n):
                while True:
                    # Try will only find valid solutions
                    try:
                        # Initializing k-means district with random batteries
                        original_district = copy.deepcopy(d)
                        initializing_district = K_means(original_district)
                        k_means_district = initializing_district.run()

                        # Saving results
                        list_results.append(k_means_district.costs_shared)
                        list_districts.append(k_means_district)
                        break

                    except NoBatteryError:
                        pass

            # Plots results 
            plot_results(list_results)
            
            j = 0
            lowest_cost = 50000
            lowest_cost_district = None

            # Will check what is the most efficient  
            for j in range(len(list_results)):
                if list_results[j] < lowest_cost:
                    lowest_cost = list_results[j]
                    lowest_cost_district = list_districts[j]
                j += 1

            # Will  print average and lowest cost.            
            print(sum(list_results) / len(list_results))
            print(lowest_cost_district.costs_shared)
            print(lowest_cost_district)
            self.choose_climber(lowest_cost_district)

    def choose_climber(self, district):
        while True:
            hillclimber_input = input('Do you want to optimize the cheapest district using Hillclimber? Or do you want to visualize the district (Hillclimber/Visualize)')
            hillclimber_answer = hillclimber_input.lower()
            if hillclimber_answer == 'hillclimber':
                break
            elif hillclimber_answer == 'visualize':
                print(district)
                print('Visualizing.')
                visualise(district)
                quit()

            print('Not the right input.')

        climber = Hillclimber(district)
        climber_district = climber.run()
        print(climber_district)
        print(f"Costs shared: {climber_district.costs_shared}")
        print("Visualizing")        
        a = visualise(climber_district)
        print("Visualized district.")
        return a

    def choose_district(self):
        district_dict = {
            '1': 'data/Huizen&Batterijen/district_1/district-1_',
            '2': 'data/Huizen&Batterijen/district_2/district-2_',
            '3': 'data/Huizen&Batterijen/district_3/district-3_'
        }
        print('Welcome to SmartGrid algorithms')
        print('==========')
        while True:
            # Askking user of input
            what_district = input('What district do you want to run?\nChoices are: 1, 2, 3\n')
            if what_district in district_dict.keys():
                break
            print('Retry please.')
        battery_csv = 'batteries.csv'
        houses_csv = 'houses.csv'

        # Crossreferencing with dict
        battery_file = district_dict[what_district] + battery_csv
        houses_file = district_dict[what_district] + houses_csv

        # File loader
        list_all_objects = []
        list_battery_objects = self.load_battery_file(battery_file)
        list_house_objects = self.load_house_file(houses_file)
        list_all_objects.append(list_battery_objects)
        list_all_objects.append(list_house_objects)
        print(f"Loaded District {what_district}.\n\n")
        return list_all_objects
            
    def load_battery_file(self, filename):
        """Loads the batteries into objects from .csv files."""
        list_battery_objects = []

        # Reads lines
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            id_loop = 1
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    coordinates = row[0]
                    capacity = row[1]
                    list_coordinates = coordinates.split(",")
                    x_coordinate = int(list_coordinates[0])
                    y_coordinate = int(list_coordinates[1])
                    
                    # Initializing battery object with reader, each line is object
                    b = Battery(id_loop, x_coordinate, y_coordinate, capacity)
                    list_battery_objects.append(b)

                    line_count += 1
                    id_loop += 1

            return list_battery_objects

    def load_house_file(self, filename):
        """Loads the house objects from the csv files."""

        # Reads lines
        with open(filename) as csv_file:
            list_house_objects = []
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    x_coordinate = int(row[0])
                    y_coordinate = int(row[1])
                    output = float(row[2])

                    # Initializing house objects with the reader, each line is object
                    h = House(line_count, x_coordinate, y_coordinate, output)
                    list_house_objects.append(h)
                    line_count += 1

            return list_house_objects

