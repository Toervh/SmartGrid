import csv
from code.classes.battery import Battery
from code.classes.house import House
from code.classes.district import District
from code.functions.readfile import load_battery_file, load_house_file
import matplotlib.pyplot as plt


if __name__ == '__main__':
    list_battery_objects = load_battery_file('data/Huizen&Batterijen/district_1/district-1_batteries.csv')
    list_house_objects = load_house_file('data/Huizen&Batterijen/district_1/district-1_houses.csv')

    d = District(list_house_objects, list_battery_objects)
    print(d)


    #Plotting the batteries and houses

    #Creating an empty plot
    x = range(60)
    y = range(60)
    plt.plot(x,y)
    plt.show()
    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    #Adding batteries
    batteries = d.batteries
    for battery in batteries:
        battery.x_coordinate = x
        battery.y_coordinate = y
        print(x, y)
        ax1.scatter(x, y, c="r", label='batteries')

    #Adding houses
    houses = d.houses
    for house in houses:
        house.x_coordinate = x
        house.y_coordinate = y
        ax1.scatter(x, y, c="b", label='houses')
