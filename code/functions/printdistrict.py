def print_district(district):
    for battery in district.batteries:
        print(battery.id)
        print(battery.x_coordinate)
        print(battery.y_coordinate)
        print(battery.capacity)
        for id in battery.houses:
            print(id)
        print(battery.houses)

    for house in district.houses:
        print(f"house id: {house.id}")
        print(f"house x coordinate: {house.x_coordinate}")
        print(f"house y coordinate: {house.y_coordinate}")
        print(f"house output: {house.output}")
        print(f"house connected battery: {house.connected_battery}")
        #print(f"house connected battery ID: {house.connected_battery.id}")
        for cable in house.cables:
            print(cable)
        if house.cables == None:
            print("No cables attached")