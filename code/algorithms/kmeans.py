from code.classes.cable import Cable
from code.functions.lay_cables import create_cable
from code.functions.find_closest_cable import find_closest_cable
from code.functions.random_battery import random_battery
from code.classes.exceptions import NoBatteryError
from code.functions.visualise import visualise
from code.functions.check_grid import check_grid
from code.classes.battery import Battery
from code.functions.swap import swap
import time
import copy

def k_means(district):

    random_coordinates = random_battery()
    new_district = district

    # print("starting new")
    # time.sleep(4)
    # making list for batteries. Important when implementing constraints.
    new_list = []
    for battery in new_district.batteries:
        new_list.append(battery)
        battery.set_imerseIII()

    i = 0
    for i in range(5):
        new_list[i].x_coordinate = random_coordinates[i][0]
        new_list[i].y_coordinate = random_coordinates[i][1]
        i+=1


    # Setting max parameters for start loop which searches for closest battery.
    grid = 50*50


    previous_list = []
    # a = visualise(new_district)

    while True:

        current_list = []
        current_battery = None
        for battery in new_district.batteries:
            battery.current_capacity = 0

        # Reset the lists of attached houses for every battery.
        for battery in new_district.batteries:
            battery.houses_objects = []
            battery.houses = []

        for house in new_district.houses:
            selected_battery = None
            closest_difference = grid

            current_x = house.x_coordinate
            current_y = house.y_coordinate
            for battery in new_district.batteries:

                battery_x = battery.x_coordinate
                battery_y = battery.y_coordinate

                x_difference = abs(current_x - battery_x)
                y_difference = abs(current_y - battery_y)
                total_difference = abs(x_difference + y_difference)

                if total_difference < closest_difference:
                    closest_difference = total_difference
                    selected_battery = battery

            battery_check = selected_battery.check_capacity(house.output)
            print(f"House: {house.id} connected battery: {selected_battery.id}. type: {selected_battery.type} capacity: {selected_battery.current_capacity}")

        # for battery in new_district.batteries:
        #     print(f"battery:{battery.id}. Capacity: {battery.current_capacity}")

            if battery_check is False:
                print(f"type: {battery.type}")
                if selected_battery.type == "PowerStar" or selected_battery.type == "Imerse-II":
                    print("upgrading")
                    selected_battery.upgrade()


                else:
                    print(f"creating new battery")
                    new_battery = Battery(len(new_district.batteries)+1, selected_battery.x_coordinate + 1, selected_battery.y_coordinate + 1, 0)
                    print(f"created new battery. ID: {new_battery.id}")
                    new_battery.set_powerstar()
                    new_district.batteries.append(new_battery)
                    selected_battery = new_battery



            selected_battery.update_capacity(house.output)
            house.connected_battery = selected_battery
            selected_battery.add_houses(house.id)
            selected_battery.add_houses_objects(house)

        # let user know a succesfull grouping was made
        # print("Connected once")

        for battery in new_district.batteries:
            x_list = []
            y_list = []
            for house in battery.houses_objects:
                x_list.append(house.x_coordinate)
                y_list.append(house.y_coordinate)

            try:
                x_average = int(sum(x_list)/len(x_list))
            except ZeroDivisionError:
                    x_average = 0
            try:
                y_average = int(sum(y_list)/len(y_list))
            except ZeroDivisionError:
                y_average = 0
            battery.x_coordinate = x_average
            battery.y_coordinate = y_average
            current_list.append((x_average, y_average))

        # print(f"previous list: {previous_list}")
        # print(f"corrected list: {current_list}")
        # a = visualise(new_district)

        if not previous_list:
            previous_list = current_list
        elif previous_list:
            if previous_list == current_list:
                check_grid(current_list, battery.houses_objects)
                break
            else:
                previous_list = current_list


        print("One iteration finished.")
        # time.sleep(5)

    for battery in new_district.batteries:
        if battery.type == "Imerse-III":
            if battery.current_capacity <= 900:
                battery.downgrade()
                print("Downgrading from imerse-III to Imerse-II")
                print(battery.type)
        if battery.type == "Imerse-II":
            if battery.current_capacity <= 450:
                battery.downgrade()
                print("Downgrading from Imerse-II to PowerStar")
                print(battery.type)
        new_district.costs_shared += battery.price

        for house in battery.houses_objects:

            closest_cable = find_closest_cable(battery, house)
            create_cable(house.x_coordinate, house.y_coordinate, closest_cable.x_coordinate, closest_cable.y_coordinate, new_district, house, battery)

    for house in new_district.houses:
        print(f"house ID: {house.id}. connected to: {house.connected_battery.id}")
    print(f"nr of batteries: {len(new_district.batteries)}")
    for battery in new_district.batteries:
        print(f"battery id: {battery.id}. type: {battery.type}. max capacity: {battery.capacity}. current: {battery.current_capacity}. x: {battery.x_coordinate} y: {battery.y_coordinate}")
    # Swap function to be perfected. after done this piece of code will see if there are available swaps that enhance
    # Efficiency.

    # new_district.shuffle_houses()
    # for house in new_district.houses:
    #     print(f"old battery = {house.connected_battery.id}")
    #     house_swap = swap(house, new_district)
    #     if house_swap:
    #
    #         print(f"house: {house.id} swapped. new battery: {house.connected_battery.id}")
    # for battery in new_district.batteries:
    #     print(f"battery {battery.id}. capacity: {battery.current_capacity}")


    print("Finished plotting.")
    print(f"costs shared: {new_district.costs_shared}")
    return new_district