class House:
    def __init__(self, x_coordinate, y_coordinate, output):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.output = output
        self.connected_battery = None
        self.cables = []

# TODO add function battery
    def add_connected_battery(self):
        pass
# TODO add cables function
    def add_cables(self, location):
        pass