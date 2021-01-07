import csv
from code.classes.battery import Battery
from code.classes.house import House
from code.classes.district import District
import matplotlib.pyplot as plt




list_house_objects = []
list_battery_objects = []

with open('data/Huizen&Batterijen/district_1/district-1_batteries.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    id_loop = 1
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'Coordinates are: {row[0]}, Capacity is: {row[1]}.')

            coordinates = row[0]
            capacity = row[1]
            list_coordinates = coordinates.split(",")
            x_coordinate = int(list_coordinates[0])
            y_coorinate = int(list_coordinates[1])


            b = Battery(id_loop, x_coordinate, y_coorinate, capacity)
            list_house_objects.append(b)

            line_count += 1
            id_loop += 1

        print(f'Processed {line_count} lines.')

with open('data/Huizen&Batterijen/district_1/district-1_houses.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'Coordinates are: {row[0]}, {row[1]}. Output is: {row[2]}.')

            x_coordinate = row[0]
            y_coorinate = row[1]
            output = float(row[2])
            print(output)

            h = House(x_coordinate, y_coorinate, output)
            list_house_objects.append(h)
            line_count += 1

d = District(list_house_objects,list_battery_objects)


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
