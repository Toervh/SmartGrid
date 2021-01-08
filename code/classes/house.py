class House:
    def __init__(self, id, x_coordinate, y_coordinate, output):
        self.id = id
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.output = output
        self.connected_battery = None
        self.cables = []


    def add_connected_battery(self, battery):
        self.connected_battery = battery


# TODO add cables function
    def add_cables(self, location):
        pass

    def __str__(self):
        return '{x_coordinate},{y_coordinate}'.format(**self.__dict__)