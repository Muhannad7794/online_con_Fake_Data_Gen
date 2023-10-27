# from person_gen import generate_random_person
# from birthDate_gen import generate_random_birthdate
from .CPR_gen import generate_random_cpr


def person_basic_info_formatted():
    # person = generate_random_person()
    # gender = person[2]
    # birth_day = generate_random_birthdate()
    profile = generate_random_cpr()

    person = profile[0]
    full_name = f'{person[0]} {person[1]}'
    gender = person[2]
    birth_day = profile[1]
    cpr = profile[2]
    basic_info = f"Full Name: {full_name}\nGender: {gender}\nBirth Date: {birth_day}\nCPR: {cpr}"
    return basic_info


# bisic_info = person_basic_info_formatted()
# print(bisic_info)
