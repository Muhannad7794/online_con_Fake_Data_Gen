from .person_gen import generate_random_person
from .birthDate_gen import generate_random_birthdate
from random import choice


def generate_random_cpr():
    birth_day = generate_random_birthdate()
    person = generate_random_person()
    gender = person[2]

    f_num_list = []
    m_num_list = []

    for i in range(00, 100):
        if i % 2 == 0:
            f_num_list.append(i)
        else:
            m_num_list.append(i)

    if gender == "female":
        f_ext = choice(f_num_list)
        cpr = f'{birth_day}-{f_ext:02d}'
    elif gender == "male":
        m_ext = choice(m_num_list)
        cpr = f'{birth_day}-{m_ext:02d}'
    else:
        print('Invalid input')

    cpr = cpr.replace('/', '')
    profile = [person, birth_day, cpr]
    return profile


# cpr = generate_random_cpr()
# print(cpr)
