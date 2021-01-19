def check_grid(battery_list, district):
    current_district = district
    house_list = []
    for house in district.houses:
        house_list.append((house.x_coordinates, house.y_coordinates))


    for element in battery_list:
        for i in house_list:
            if element == house_list[i]:
                element[0]+=1
                check_grid(battery_list, current_district)
    return battery_list