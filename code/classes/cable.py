class Cable:
    def __init__(self, start_x_coordinate, start_y_coordinate, end_x_coordinate, end_y_coordinate, district, house):
        self.x_coordinates = []
        self.y_coordinates = []
        self.xy_coordinates = []

        self.start_x_coordinate = int(start_x_coordinate)
        self.start_y_coordinate = int(start_y_coordinate)

        if self.start_x_coordinate > end_x_coordinate:
            for x in range(end_x_coordinate, self.start_x_coordinate):
                self.x_coordinates.append(x)
                self.y_coordinates.append(start_y_coordinate)

        else:
            for x in range(self.start_x_coordinate, end_x_coordinate):
                self.x_coordinates.append(x)
                self.y_coordinates.append(start_y_coordinate)

        if self.start_y_coordinate > end_y_coordinate:
            for y in range(end_y_coordinate, self.start_y_coordinate):
                self.y_coordinates.append(y)
                self.x_coordinates.append(end_x_coordinate)
        else:
            for y in range(self.start_y_coordinate, end_y_coordinate+1):
                self.y_coordinates.append(y)
                self.x_coordinates.append(end_x_coordinate)

        for i in range(len(self.x_coordinates) - 1):
            self.xy_coordinates.append((self.x_coordinates[i], self.y_coordinates[i]))


    # def add_cables(self, house, district):

        for cable in self.xy_coordinates:
            if cable in district.cables_coordinates:
                pass

            house.cables.append((self.x_coordinates, self.y_coordinates))

            district.cables_coordinates.append(self.xy_coordinates)
            district.costs_shared += 9