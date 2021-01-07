import csv
from code.classes.battery import Battery
from code.classes.house import House


with open('data/Huizen&Batterijen/district_1/district-1_batteries.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
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

            b = Battery(x_coordinate, y_coorinate, capacity)


            line_count += 1


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

            line_count += 1
        #print(f'Processed {line_count} lines.')