from code.functions.find_closest_cable import find_closest_cable
from code.functions.lay_cables import create_cable
import copy

def swap(house, district):
    swapped = False
    cheapest_connection = (len(house.cables) * 9)
    print(f"house: {house.id},  cheapest connection: {cheapest_connection}")
    copy_house = copy.copy(house)
    copy_district = copy.copy(district)

    house_output = copy_house.output


    for battery in copy_district.batteries:
        # print(battery.current_capacity)
        copy_house.connected_battery = battery

        closest_cable = find_closest_cable(battery, copy_house)
        copy_house.cables = []
        create_cable(copy_house.x_coordinate, copy_house.y_coordinate, closest_cable.x_coordinate, closest_cable.y_coordinate, copy_district, copy_house, battery)
        cable_cost = len(copy_house.cables * 9)
        print(f"battery: {battery.id}, cable cost: {cable_cost}")
        if cable_cost < cheapest_connection:
            swapped = True
            cheapest_connection = cable_cost

            house.connected_battery = battery
            closest_cable = find_closest_cable(battery, house)
            create_cable(house.x_coordinate, house.y_coordinate, closest_cable.x_coordinate,
                         closest_cable.y_coordinate, district, house, battery)


    return swapped
