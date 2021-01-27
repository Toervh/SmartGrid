class Cable:
    """
    Cable are the segments of the manhattan grid that is needed to be visualised. It is used to calculate the costs and to visualize the network.
    """
    def __init__(self, x_coordinate, y_coordinate, xy_coordinate, battery):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.xy_coordinate = xy_coordinate
        self.connected_battery = battery