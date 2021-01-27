from code.classes.cable import Cable
from code.functions.lay_cables import create_cable
from code.functions.find_closest_cable import find_closest_cable
from code.functions.random_battery import random_battery
from code.classes.exceptions import NoBatteryError
from code.functions.check_grid import check_grid
from code.classes.battery import Battery
from code.functions.swap import swap
import random
import time
import copy

class K_means:
    """
    K-means is an algorithm that will place the most efficient batteries randomly.
    It will then look for clusters where the most efficient battery placement is. and connect the houses.
    """
    def __init__(self, district):
        self.district = copy.deepcopy(district)


    def k_means(self, district):
        random_coordinates = self.random_battery()
        new_district = district

        # making list for batteries. Important when implementing constraints.
        new_list = []
        for battery in new_district.batteries:
            new_list.append(battery)
            battery.set_imerseIII()

        i = 0
        for i in range(5):
            new_list[i].x_coordinate = random_coordinates[i][0]
            new_list[i].y_coordinate = random_coordinates[i][1]
            i+=1

        # Setting max parameters for start loop which searches for closest battery.
        grid = 50*50

        previous_list = []
        while True:

            current_list = []
            current_battery = None
            for battery in new_district.batteries:
                battery.current_capacity = 0

            # Reset the lists of attached houses for every battery.
            for battery in new_district.batteries:
                battery.houses_objects = []
                battery.houses = []


            for house in new_district.houses:

                selected_battery = None
                closest_difference = grid

                current_x = house.x_coordinate
                current_y = house.y_coordinate

                for battery in new_district.batteries:

                    battery_x = battery.x_coordinate
                    battery_y = battery.y_coordinate

                    x_difference = abs(current_x - battery_x)
                    y_difference = abs(current_y - battery_y)
                    total_difference = abs(x_difference + y_difference)

                    if total_difference < closest_difference:
                        closest_difference = total_difference
                        selected_battery = battery

                battery_check = selected_battery.check_capacity(house.output)

                if battery_check is False:

                    if selected_battery.type == "PowerStar" or selected_battery.type == "Imerse-II":
                        selected_battery.upgrade()

                    else:
                        new_battery = Battery(len(new_district.batteries)+1, selected_battery.x_coordinate + 1, selected_battery.y_coordinate + 1, 0)
                        new_battery.set_powerstar()
                        new_district.batteries.append(new_battery)
                        selected_battery = new_battery

                selected_battery.update_capacity(house.output)
                house.connected_battery = selected_battery
                selected_battery.add_houses(house.id)
                selected_battery.add_houses_objects(house)

            for battery in new_district.batteries:
                x_list = []
                y_list = []
                for house in battery.houses_objects:
                    x_list.append(house.x_coordinate)
                    y_list.append(house.y_coordinate)

                try:
                    x_average = int(sum(x_list)/len(x_list))
                except ZeroDivisionError:
                        x_average = 0
                try:
                    y_average = int(sum(y_list)/len(y_list))
                except ZeroDivisionError:
                    y_average = 0
                battery.x_coordinate = x_average
                battery.y_coordinate = y_average
                current_list.append((x_average, y_average))

            if not previous_list:
                previous_list = current_list
            elif previous_list:
                if previous_list == current_list:
                    check_grid(current_list, battery.houses_objects)
                    break
                else:
                    previous_list = current_list

            # print("One iteration finished.")
            # time.sleep(5)

        for battery in new_district.batteries:
            if battery.type == "Imerse-III":
                if battery.current_capacity <= 900:
                    battery.downgrade()
            if battery.type == "Imerse-II":
                if battery.current_capacity <= 450:
                    battery.downgrade()
            new_district.costs_shared += battery.price

            for house in battery.houses_objects:

                closest_cable = find_closest_cable(battery, house)
                list_cables = create_cable(house.x_coordinate, house.y_coordinate, closest_cable.x_coordinate, closest_cable.y_coordinate, new_district, house, battery)

        for house in new_district.houses:
            new_district.update_cost(len(house.cables), 9)
        for battery in new_district.batteries:
            new_district.update_cost(1, battery.price)

        print("Finished plotting.")
        print(f"costs shared: {new_district.costs_shared}")
        return new_district

    def random_battery(self):
        """
        Generates random positions for the battery, each in one quadrant of the grid and one 'wildcard' that will be placed somewhere totally random on the grid.
        """
        random_coordinates = []

        district_1_min_x = random.randrange(0, 25, 1)
        district_1_min_y = random.randrange(0, 25, 1)
        
        district_2_min_x = random.randrange(25,50,1)
        district_2_min_y = random.randrange(0,25,1)
        
        district_3_min_x = random.randrange(0,25,1)
        district_3_min_y = random.randrange(25,50,1)

        district_4_min_x = random.randrange(25,50,1)
        district_4_min_y = random.randrange(25,50,1)

        district_5_min_x = random.randrange(0,50,1)
        district_5_min_y = random.randrange(0,50,1)
            
        random_coordinates.append((district_1_min_x, district_1_min_y)) 
        random_coordinates.append((district_2_min_x, district_2_min_y)) 
        
        random_coordinates.append((district_3_min_x, district_3_min_y))
        random_coordinates.append((district_4_min_x, district_4_min_y))
        
        random_coordinates.append((district_5_min_x, district_5_min_y))
        
        return random_coordinates

    def run(self):
        initializing_district = self.district
        k_means_district = self.k_means(initializing_district)
        return k_means_district
