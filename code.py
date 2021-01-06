import csv

class Battery:
    def __init__(self, x_coordinate, y_coordinate, tatal_capacity, used_capacity, num_connections):


with open('Huizen&Batterijen/district_1/district-1_batteries.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'Coordinates are: {row[0]}, Capaciteit is: {row[1]}.')
            Battery({row[0]}, {row[0]}, {row[1]}, 0, 0)
            print(Createbattery)
            line_count += 1
        print(f'Processed {line_count} lines.')
