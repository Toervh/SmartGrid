import random

def random_battery():
    random_coordinates = []

    district_1_min_x = random.randrange(0, 25, 1)
    district_1_min_y = random.randrange(0, 25, 1)
    
    district_2_min_x = random.randrange(25,50,1)
    district_2_min_y = random.randrange(0,25,1)
    
    district_3_min_x = random.randrange(0,25,1)
    district_3_min_y = random.randrange(25,50,1)

    district_4_min_x = random.randrange(25,50,1)
    district_4_min_y = random.randrange(25,50,1)

    district_5_min_x = random.randrange(0,50,1)
    district_5_min_y = random.randrange(0,50,1)
        
    random_coordinates.append((district_1_min_x, district_1_min_y)) 
    random_coordinates.append((district_2_min_x, district_2_min_y)) 
    
    random_coordinates.append((district_3_min_x, district_3_min_y))
    random_coordinates.append((district_4_min_x, district_4_min_y))
    
    random_coordinates.append((district_5_min_x, district_5_min_y))
    
    return random_coordinates

random_battery()

