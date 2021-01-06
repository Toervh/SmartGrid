import csv

class District:
    def __init__(self, cost_shared):
        self.cost_shared = cost_shared

class House:
    def __init__(self, location, output, cables):
        self.location = location
        self.output = output
        self.cables = cables

    #def add_cables

class Battery:
    def __init__(self, location, capacity, houses):
        self.location = location
        self.capacity = capacity
        self.houses = houses

    #def add_houses




with open('Huizen&Batterijen/district_1/district-1_batteries.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'Coordinates are: {row[0]}, Capaciteit is: {row[1]}.')
            line_count += 1
        print(f'Processed {line_count} lines.')

with open('Huizen&Batterijen/district_1/district-1_houses.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'Coordinates are: {row[0]}, Output is: {row[1]}.')
            line_count += 1
        print(f'Processed {line_count} lines.')