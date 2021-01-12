class Battery:
    def __init__(self, id, x_coordinate, y_coordinate, capacity):

        self.id = id
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.capacity = float(capacity)
        self.current_capacity = 0.0
        self.houses = []
        self.houses_objects = []
        self.cables = []

    def add_houses(self, house_id):
        self.houses.append(house_id)

    def add_houses_objects(self, house):
        self.houses_objects.append(house)

    def check_capacity(self, output):
        fl_output = float(output)
        if self.current_capacity + fl_output > self.capacity:
            return False
        return True

    def update_capacity(self, output):

        fl_output = float(output)
        self.current_capacity += fl_output
        return True


    def return_x(self):
        list_x = list(self.x_coordinate)
        return list_x

    def __repr__(self):
        return str(self.current_capacity)

    def __str__(self):
        return '{x_coordinate},{y_coordinate}'.format(**self.__dict__)

    def return_y(self):
        list_y = list(self.y_coordinate)
        return list_y
