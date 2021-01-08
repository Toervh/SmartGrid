import csv
from code.classes.battery import Battery
from code.classes.house import House
from code.classes.district import District


def load_battery_file(filename):
    list_battery_objects = []
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
                y_coorinate = int(list_coordinates[1])

                b = Battery(id_loop, x_coordinate, y_coorinate, capacity)
                list_battery_objects.append(b)

                line_count += 1
                id_loop += 1

        return list_battery_objects

def load_house_file(filename):
    with open(filename) as csv_file:
        list_house_objects = []
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                x_coordinate = row[0]
                y_coorinate = row[1]
                output = float(row[2])

                h = House(line_count, x_coordinate, y_coorinate, output)
                list_house_objects.append(h)
                line_count += 1

        return list_house_objects