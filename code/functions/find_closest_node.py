from code.classes.node import Node

def find_closest_node(district, house):


    current_x = house.x_coordinate
    current_y = house.y_coordinate

    max_difference = int(50 * 50)

    closest_difference = max_difference
    selected_battery = None
    closest_node = None


    for battery in district.batteries:
        if not battery.check_capacity(house.output):
            continue

        for cable in battery.cables:
            cable_x = cable.x_coordinate
            cable_y = cable.y_coordinate

            x_difference = abs(current_x - cable_x)
            y_difference = abs(current_y - cable_y)
            total_difference = abs(x_difference + y_difference)

            if total_difference < closest_difference:
                closest_difference = total_difference
                selected_battery = battery
                closest_node = Node(cable_x, cable_y, battery)


        battery_x = battery.x_coordinate
        battery_y = battery.y_coordinate

        x_difference = abs(current_x - battery_x)
        y_difference = abs(current_y - battery_y)

        total_difference = abs(x_difference + y_difference)


        if total_difference < closest_difference:
            closest_difference = total_difference
            selected_battery = battery
            closest_node = Node(battery.x_coordinate, battery.y_coordinate, battery)

    house.add_connected_battery(selected_battery)
    selected_battery.add_houses(house.id)
    selected_battery.add_houses_objects(house)
    selected_battery.update_capacity(house.output)


    return closest_node