

def lay_cables(district):
    list_houses = list(district.houses)
    list_houses_x_coordinates = []
    for house in list_houses:
        list_houses_x_coordinates.append(house.x_coordinate)
    list_houses_y_coordinates = []
    for house in list_houses:
        list_houses_y_coordinates.append(house.y_coordinate)

    list_batteries = list(district.batteries)
    list_batteries_x_coordinates = []
    for battery in list_batteries:
        list_batteries_x_coordinates.append(battery.x_coordinate)
    list_batteries_y_coordinates = []
    for battery in list_batteries:
        list_batteries_y_coordinates.append(battery.y_coordinate)

    battery_dict = {}
    for battery in list_batteries:
        list_house = []
        battery_dict[battery.id] = list_house
        for house in battery.houses_objects:
            list_house.append((house.x_coordinate, house.y_coordinate))

    for house in district.houses:

        current_x_coordinate = house.x_coordinate
        current_y_coordinate = house.y_coordinate

        for i in battery_dict.keys():
        current_battery = battery_dict.get(i, None)
        j = 0
        while j < len(current_battery):
            current_house = current_battery[j]
                p.step([list_batteries_x_coordinates[i - 1], current_house[0]],
                       [list_batteries_y_coordinates[i - 1], current_house[1]], line_width=1)
            j += 1
        i += 1

        while current_x_coordinate is not house.connected_battery.x_coordinate and current_y_coordinate is not house.connected_battery.y_coordinate:
            if current_x_coordinate < house.connected_battery.x_coordinate:
                current_x_coordinate += 1
                district.add_cable(current_x_coordinate, current_y_coordinate, house)

            if current_y_coordinate < house.connected_battery.y_coordinate:
                current_y_coordinate += 1
                district.add_cable(current_x_coordinate, current_y_coordinate, house)
