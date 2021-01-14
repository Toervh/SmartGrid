from code.classes.cable import Cable

def create_cable(start_x_coordinate, start_y_coordinate, end_x_coordinate, end_y_coordinate, district, house, battery):

    x_coordinates = []
    y_coordinates = []
    xy_coordinates = []

    start_x_coordinate = int(start_x_coordinate)
    start_y_coordinate = int(start_y_coordinate)

    if start_x_coordinate > end_x_coordinate:
        for x in range(end_x_coordinate, start_x_coordinate):
            x_coordinates.append(x)
            y_coordinates.append(start_y_coordinate)

    else:
        for x in range(start_x_coordinate, end_x_coordinate):
            x_coordinates.append(x)
            y_coordinates.append(start_y_coordinate)

    if start_y_coordinate > end_y_coordinate:
        for y in range(end_y_coordinate, start_y_coordinate):
            y_coordinates.append(y)
            x_coordinates.append(end_x_coordinate)
    else:
        for y in range(start_y_coordinate, end_y_coordinate + 1):
            y_coordinates.append(y)
            x_coordinates.append(end_x_coordinate)

    for i in range(len(x_coordinates) - 1):
        xy_coordinates.append((x_coordinates[i], y_coordinates[i]))

    for cable in xy_coordinates:
        if cable in battery.cables:
            xy_coordinates.remove(cable)
        district.costs_shared += 9

    for i in range(len(xy_coordinates)):
        cable = Cable(x_coordinates[i], y_coordinates[i], xy_coordinates[i], battery)
        house.cables.append(cable)
        district.cables_coordinates.append(cable)
        battery.cables.append(cable)
