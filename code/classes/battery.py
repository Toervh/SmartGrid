class Battery:
    def __init__(self, id, x_coordinate, y_coordinate, capacity):

        self.id = id
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.capacity = capacity
        self.current_capacity = 0
        self.houses = []
        self.houses_objects = []

    def add_houses(self, house_id):
        self.houses.append(house_id)

    def add_houses_objects(self, house):
        self.houses_objects.append(house)

    def return_x(self):
        list_x = list(self.x_coordinate)
        return list_x

    def __repr__(self):
        return self.id

    def __str__(self):
        return '{x_coordinate},{y_coordinate}'.format(**self.__dict__)

    def return_y(self):
        list_y = list(self.y_coordinate)
        return list_y

    #TODO implement update capacity