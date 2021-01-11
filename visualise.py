import csv
from code.classes.battery import Battery
from code.classes.house import House
from code.classes.district import District
import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_file, show

def visualise(district):
    list_houses = list(district.houses)
    list_houses_x_coordinates = []
    for house in list_houses:
        list_houses_x_coordinates.append(house.x_coordinate)
    list_houses_y_coordinates = []
    for house in list_houses:
        list_houses_y_coordinates.append(house.y_coordinate)

    list_batteries = list(district.batteries)
    list_batteries_x_coordinates = []
    for battery in list_batteries:
        list_batteries_x_coordinates.append(battery.x_coordinate)
    list_batteries_y_coordinates = []
    for battery in list_batteries:
        list_batteries_y_coordinates.append(battery.y_coordinate)

    output_file("plot.html")

    p = figure(title="Power Grid", x_axis_label='x', y_axis_label='y')
    p.square(list_batteries_x_coordinates, list_batteries_y_coordinates, size=20, color="blue", alpha=0.5)
    p.circle(list_houses_x_coordinates, list_houses_y_coordinates, size=10, color="red", alpha=0.5)


    battery_dict = {}
    for battery in list_batteries:
        list_house = []
        battery_dict[battery.id] = list_house
        for house in battery.houses_objects:
            list_house.append((house.x_coordinate, house.y_coordinate))

    print(battery_dict)

    for i in battery_dict.keys():
    current_battery = battery_dict.get(i, None)
        j = 0
        while j < len(current_battery):
            current_house = current_battery[j]
            p.step([list_batteries_x_coordinates[i - 1], current_house[0]], [list_batteries_y_coordinates[i - 1], current_house[1]], line_width=1)
            j+=1
        i+=1

    return(show(p))



