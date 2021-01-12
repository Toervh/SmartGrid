class Cable:
    def __init__(self, start_x_coordinate, start_y_coordinate, end_x_coordinate, end_y_coordinate):
        self.x_coordinates = []
        self.y_coordinates = []

        #maak code voor achteruit of min lopen

        for x in range(start_x_coordinate, end_x_coordinate):
            self.x_coordinates.append(x)
            self.y_coordinates.append(start_y_coordinate)

        for y in range(start_y_coordinate, end_y_coordinate+1):
            self.y_coordinates.append(y)
            self.x_coordinates.append(end_x_coordinate)

if __name__ == '__main__':
    a = Cable(22,2,4,40)
    print(a.x_coordinates)
    print(a.y_coordinates)