from random import randint


def generate_random_birthdate():

    day = randint(1, 28)
    month = randint(1, 12)
    year = randint(1930, 2003)
    birht_date = f'{day:02d}/{month:02d}/{year % 100:02d}'
    return birht_date


birthday = generate_random_birthdate()
print(birthday)
