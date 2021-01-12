import csv
from code.classes.battery import Battery
from code.classes.house import House
from code.classes.district import District
from code.classes.cable import Cable
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

    # print(f"battery dict: {battery_dict}")

    # for i in battery_dict.keys():
    #     current_battery = battery_dict.get(i, None)
    #     j = 0
    #     while j < len(current_battery):
    #         current_house = current_battery[j]
    #         p.step([list_batteries_x_coordinates[i - 1], current_house[0]], [list_batteries_y_coordinates[i - 1], current_house[1]], line_width=1)
    #         j+=1
    #     i+=1


    # cables = district.cables_coordinates
    # current_cable = cables[0]
    # begin = current_cable[0]
    # end = current_cable[-1]
    # print(current_cable)
    # print(begin)
    # print(begin[0])
    # print(begin[1])
    # print(type(begin[1]))
    # print(end)
    # print(end[0])
    # print(end[1])

    cables = district.cables_coordinates
    for current_cable in cables:
        begin_coordinates = current_cable[0]
        end_coordinates = current_cable[-1]
        begin_x = begin_coordinates[0]
        begin_y = int(begin_coordinates[1])
        end_x = end_coordinates[0]
        end_y = end_coordinates[1]
        p.step([begin_x, end_x], [begin_y, end_y], line_width=1)
    
    return(show(p))


