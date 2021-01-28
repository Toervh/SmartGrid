from code.classes.district import District
from code.functions.prompts import Prompt
import random

if __name__ == '__main__':
    prompting = Prompt()
    district_chosen = prompting.choose_district()
    prompting.choose_algorithm(district_chosen[1], district_chosen[0])
