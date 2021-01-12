from code.classes.cable import Cable

def closest_assignment(district):


    for house in district.houses:

        current_x = house.x_coordinate
        current_y = house.y_coordinate

        max_difference = int(50 * 50)

        closest_difference = max_difference
        closest_battery = None

        list_available_batteries = []
        for battery in district.batteries:
            if battery.check_capacity(house.output):
                list_available_batteries.append(battery)

            for available_battery in list_available_batteries:
                battery_x = available_battery.x_coordinate
                battery_y = available_battery.y_coordinate

                x_difference = abs(current_x - battery_x)
                y_difference = abs(current_y - battery_y)

                total_difference = abs(x_difference + y_difference)
                if total_difference < closest_difference:
                    closest_difference = total_difference
                    closest_battery = available_battery

        house.add_connected_battery(closest_battery)
        closest_battery.add_houses(house.id)
        closest_battery.add_houses_objects(house)
        closest_battery.update_capacity(house.output)
        print(f"house: {house}, closest unfilled battery: {closest_battery}, distance: {closest_difference}")

        cable = Cable(house.x_coordinate, house.y_coordinate, closest_battery.x_coordinate, closest_battery.y_coordinate,
                  district, house, closest_battery)

    closest_district = district

    return closest_district