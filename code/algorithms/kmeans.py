from code.classes.cable import Cable
from code.functions.lay_cables import create_cable
from code.functions.find_closest_cable import find_closest_cable
from code.functions.random_battery import random_battery
from code.classes.exceptions import NoBatteryError
import copy

def k_means(district):
    random_coordinates = random_battery()
    new_district = copy.deepcopy(district)
    new_list = []

    for battery in district.batteries:
        new_list.append(battery)
    
    #NIET LOOPEN
    i = 0
    for i in range(4):
        new_list[i].x_coordinate = random_coordinates[i][0]
        new_list[i].y_coordinate = random_coordinates[i][1]
        i+=1
    grid = 50*50
    closest_difference = grid
    while True:
        current_list = []
        previous_list = []
        current_battery = None
        for house in district.houses:
            selected_battery = None
            closest_difference = grid

            current_x = house.x_coordinate
            current_y = house.y_coordinate
            for battery in district.batteries:
                
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
            #battery_dict[k].append((house.x_coordinate, house.y_coordinate))

        x_list = []
        y_list = []

        for battery in district.batteries:
            for house in battery.houses_objects:
                i = 0
                print(f"House number: {i} {house.x_coordinate}")
                x_list.append(house.x_coordinate)
                y_list.append(house.y_coordinate)
                i+=1
            x_average = int(sum(x_list)/len(x_list))
            y_average = int(sum(y_list)/len(y_list))
            battery.x_coordinate = x_average
            battery.y_coordinate = y_average
            current_list.append((x_average, y_average))
        if not previous_list:
            previous_list = current_list
        elif previous_list:
            if previous_list == current_list:
                break
            else:
                previous_list = current_list
            
                i = 0
                for i in range(4):
                    battery.x_coordinate = current_list[i][0]
                    battery.y_coordinate = current_list[i][1]
                    i+=1


    for battery in district.batteries:
        for house in battery.houses:
            create_cable(battery.x_coordinate, battery.y_coordinate, house.x_coordinate, house.y_coordinate, district, house, battery)