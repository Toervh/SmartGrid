from code.classes.node import Node
from code.classes.exceptions import NoBatteryError

def find_closest_node(district, house):

    # Gets X and Y coordinates of the house
    current_x = house.x_coordinate
    current_y = house.y_coordinate

    # Create max difference so we can compare the first battery to the max difference
    max_difference = int(50 * 50)
    closest_difference = max_difference

    # Set selected battery to None, this will be adjusted when the closest node is found.
    selected_battery = None
    closest_node = None

    # Create empty list which we will fill with all batteries that can handle the Houses Output.
    available_batteries = []

    # Loop over every battery to see if they can handle the output
    for battery in district.batteries:
        if battery.check_capacity(house.output):
            available_batteries.append(battery)

    # If there is no available battery the program should return False so it can end.
    if available_batteries == []:
        raise NoBatteryError

    # For every available battery: Check if for the closest cable to the houses coordinates.
    previous_battery = None
    for battery in available_batteries:
        for cable in battery.cables:
            cable_x = cable.x_coordinate
            cable_y = cable.y_coordinate

            x_difference = abs(current_x - cable_x)
            y_difference = abs(current_y - cable_y)
            total_difference = abs(x_difference + y_difference)

            # If the cable is closest: set it as closest difference,
            # set the battery it belongs to to selected battery
            # and create the node for easy access to this point.
            if total_difference < closest_difference:
                closest_difference = total_difference
                selected_battery = battery
                closest_node = Node(cable_x, cable_y, battery)

        previous_battery = battery

        # Do the same as above but for the coordinates of every battery instead of the cables.
        # This is especially important when there are few cables of the grid.
        battery_x = battery.x_coordinate
        battery_y = battery.y_coordinate

        x_difference = abs(current_x - battery_x)
        y_difference = abs(current_y - battery_y)

        total_difference = abs(x_difference + y_difference)

        # If the battery is closest: set it as closest difference for comparison,
        # set the battery as selected battery
        # and create the node for easy access to this point.
        if total_difference < closest_difference:
            closest_difference = total_difference
            selected_battery = battery
            closest_node = Node(battery.x_coordinate, battery.y_coordinate, battery)

    # Add the connection to all Classes.
    # TODO Optimize this.
    house.add_connected_battery(selected_battery)
    selected_battery.add_houses(house.id)
    selected_battery.add_houses_objects(house)
    selected_battery.update_capacity(house.output)


    return closest_node