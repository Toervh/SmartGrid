def check_grid(battery_list, house_objects):
    house_list = []
    house_layout = house_objects
    for house in house_objects:
        house_list.append([house.x_coordinate, house.y_coordinate])

    for element in battery_list:
        for house in house_list:
            if element == house:     
                element[0]+=1
                check_grid(battery_list, house_layout)
    return battery_list