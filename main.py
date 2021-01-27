from code.classes.district import District
from code.functions.prompts import choose_algorithm, choose_district
import random

if __name__ == '__main__':
    random.seed(2)
    # ****-------------Instantiating the object-------------****
    district_chosen = choose_district()
    d = District(id, district_chosen[1], district_chosen[0])
    choose_algorithm(district_chosen[1], district_chosen[0])
