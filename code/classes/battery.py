class Battery:
    def __init__(self, id, x_coordinate, y_coordinate, capacity):

        self.id = id
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.capacity = capacity
        self.houses = []

    def add_houses(self, house_id):
        self.houses.append(house_id)