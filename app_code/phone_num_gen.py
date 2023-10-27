from random import choice, randint

starting_digit_combo = [2, 30, 31, 40, 41, 42, 50, 51, 52, 53, 60, 61, 71, 81, 91, 92, 93, 342, 344, 349, 356, 357, 359, 362, 365, 366, 389, 398, 431, 441, 462, 466, 468, 472, 474, 476, 478, 485, 486, 488, 489, 493, 496, 498,
                        499, 542, 543, 545, 551, 552, 556, 571, 574, 577, 579, 584, 586, 587, 589, 597, 598, 627, 629, 641, 649, 658, 662, 665, 667, 692, 694, 697, 771, 772, 782, 783, 785, 786, 788, 789, 826, 827, 829]


def generate_random_phone_number():
    strarting_combo = choice(starting_digit_combo)
    starter = str(strarting_combo)
    if len(starter) == 1:
        num_tail = randint(1000000, 9999999)
        phone_number = f"+45-{starter}-{num_tail}"
        return phone_number
    elif len(starter) == 2:
        num_tail = randint(100000, 999999)
        phone_number = f"+45-{starter}-{num_tail}"
        return phone_number
    elif len(starter) == 3:
        num_tail = randint(10000, 99999)
        phone_number = f"+45-{starter}-{num_tail}"
        return phone_number
    elif len(starter) == 4:
        num_tail = randint(1000, 9999)
        phone_number = f"+45-{starter}-{num_tail}"
        return phone_number
    elif len(starter) == 5:
        num_tail = randint(100, 999)
        phone_number = f"+45-{starter}-{num_tail}"
        return phone_number
    elif len(starter) == 6:
        num_tail = randint(10, 99)
        phone_number = f"+45-{starter}-{num_tail}"
        return phone_number
    else:
        return "Starter is too long"


# phone_number = generate_random_phone_number()
# print(phone_number)
