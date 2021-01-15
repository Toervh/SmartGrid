from code.classes.cable import Cable
from code.functions.lay_cables import create_cable
from code.functions.find_closest_cable import find_closest_cable
from code.functions.random_battery import random_battery
from code.classes.exceptions import NoBatteryError
from code.functions.visualise import visualise
import time
import copy

def k_means(district):
    random_coordinates = random_battery()
    new_district = copy.deepcopy(district)

    # making list for batteries. Important when implementing constraints.
    new_list = []
    for battery in new_district.batteries:
        new_list.append(battery)


    print(f"starting coordinates: {random_coordinates}")

    i = 0
    for i in range(4):
        new_list[i].x_coordinate = random_coordinates[i][0]
        new_list[i].y_coordinate = random_coordinates[i][1]
        i+=1

    # Setting max parameters for start loop which searches for closest battery.
    grid = 50*50
    closest_difference = grid


    previous_list = []

    while True:
        current_list = []
        current_battery = None
        a = visualise(new_district)

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
            selected_battery.add_houses(house.id)
            selected_battery.add_houses_objects(house) 


        x_list = []
        y_list = []

        for battery in new_district.batteries:
            for house in battery.houses_objects:
                x_list.append(house.x_coordinate)
                y_list.append(house.y_coordinate)


            x_average = int(sum(x_list)/len(x_list))
            y_average = int(sum(y_list)/len(y_list))
            battery.x_coordinate = x_average
            battery.y_coordinate = y_average
            current_list.append((x_average, y_average))

        print(f"previous list: {previous_list}")
        print(f"corrected list: {current_list}")
        a = visualise(new_district)

        if not previous_list:
            previous_list = current_list
        elif previous_list:
            if previous_list == current_list:
                break
            else:
                previous_list = current_list


        print("One iteration finished.")
        time.sleep(20)

    for battery in new_district.batteries:
        for house in battery.houses_objects:
            create_cable(battery.x_coordinate, battery.y_coordinate, house.x_coordinate, house.y_coordinate, new_district, house, battery)
