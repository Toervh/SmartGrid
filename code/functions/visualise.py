import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_file, show

def visualise(district):
    """
    Visualise uses Bokeh to draw the grid with the houses.
    The datastructure for the houses is a dict of a list of sets of coordinates.
    The dict keys are the batteries, the list is the list of houses connected, and its
    elements are tuples of the coordinates of the houses.
    It uses scatterplot to draw the houses and uses
    steps to draw a Manhattan grid from the location of the
    house to the battery.
    """
    # Makes a list of the houses to scatterplot.
    list_houses = list(district.houses)
    list_houses_x_coordinates = []
    for house in list_houses:
        list_houses_x_coordinates.append(house.x_coordinate)
    list_houses_y_coordinates = []
    for house in list_houses:
        list_houses_y_coordinates.append(house.y_coordinate)

    # Makes a list of the batteries to scatterplot.
    list_batteries = list(district.batteries)
    list_batteries_x_coordinates = []
    list_batteries_y_coordinates = []
    for battery in list_batteries:
        list_batteries_x_coordinates.append(battery.x_coordinate)
        list_batteries_y_coordinates.append(battery.y_coordinate)

    output_file("plot.html")

    # Instantiates the graph and draws the scatterplot.
    p = figure(title="Power Grid", x_axis_label='x', y_axis_label='y')
    p.square(list_batteries_x_coordinates, list_batteries_y_coordinates, size=20, color="blue", alpha=0.5)
    p.circle(list_houses_x_coordinates, list_houses_y_coordinates, size=10, color="red", alpha=0.5)

    # Iterate over every house, and every cable attached to it.
    for house in district.houses:
        i = 0

        # Making a list, checking it twice, for getting length of amount of cables.
        list_cables = []
        for cable in house.all_cables:
            list_cables.append(cable)

        # Set length of the list for easier grabbing of X and Y to step to.
        len_list_cables = len(list_cables)

        # While there are cables in the list, plot those cables.
        while i < len_list_cables - 1:
            p.step([list_cables[i].x_coordinate, list_cables[i + 1].x_coordinate],
                   [list_cables[i].y_coordinate, list_cables[i + 1].y_coordinate], line_width=1)

            i += 1

    return show(p)