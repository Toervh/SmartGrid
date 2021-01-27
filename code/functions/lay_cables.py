from code.classes.cable import Cable

def create_cable(start_x_coordinate, start_y_coordinate, end_x_coordinate, end_y_coordinate, district, house, battery):
    """
    This function places cables (by calling the Cable class) at every node in between the start coordinates &
    end coordinates. It then appends each of those objects to the cable lists in the objects House and Battery lists.
    """

    # Create empty lists in which all coordinates in between two points are placed.
    x_coordinates = []
    y_coordinates = []
    xy_coordinates = []

    start_x_coordinate = int(start_x_coordinate)
    start_y_coordinate = int(start_y_coordinate)

    # Check if the distance between X points is negative.
    if start_x_coordinate > end_x_coordinate:
        for x in range(end_x_coordinate, start_x_coordinate):
            x_coordinates.append(x)
            y_coordinates.append(start_y_coordinate)
    # This is if the distance is positive.
    else:
        for x in range(start_x_coordinate, end_x_coordinate):
            x_coordinates.append(x)
            y_coordinates.append(start_y_coordinate)

    # Check if the distance between Y points is negative.
    if start_y_coordinate > end_y_coordinate:
        for y in range(end_y_coordinate, start_y_coordinate):
            y_coordinates.append(y)
            x_coordinates.append(end_x_coordinate)
    # Check if the distance is positive.
    else:
        for y in range(start_y_coordinate, end_y_coordinate + 1):
            y_coordinates.append(y)
            x_coordinates.append(end_x_coordinate)

    # Append both the X and Y coordinates to the XY list.
    for i in range(len(x_coordinates) - 1):
        xy_coordinates.append((x_coordinates[i], y_coordinates[i]))

    # Use the XY list to check if there were already cables at that node. If so this deletes them.
    for cable in xy_coordinates:
        if cable in battery.cables:
            xy_coordinates.remove(cable)


    # Now the list is cleared of duplicate existing nodes: Create new cables for each coordinate in XY list that is new.
    for i in range(len(xy_coordinates)):
        cable = Cable(x_coordinates[i], y_coordinates[i], xy_coordinates[i], battery)
        house.cables.append(cable)
        district.cables_coordinates.append(cable)
        battery.cables.append(cable)

    return xy_coordinates