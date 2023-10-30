from .fake_person_gen import generate_fake_person


def generate_multiple_fake_persons(number_of_persons):
    if not isinstance(number_of_persons, int):
        raise TypeError("number_of_persons must be an integer")
    elif number_of_persons <= 0:
        raise ValueError("number_of_persons must be a positive integer")
    elif number_of_persons > 100:
        raise ValueError("number_of_persons cannot be greater than 100")

    fake_persons = []
    for i in range(number_of_persons):
        fake_person = generate_fake_person()
        fake_persons.append(fake_person)

    return fake_persons


people_count = ['not an int', -1, 0, 101, 4, 10]

for count in people_count:
    try:
        count = int(count)
        people = generate_multiple_fake_persons(count)
        for person in people:
            print(person)
            print("-------------------------------------------------------------------\n")
    except ValueError as e:
        print(f"Error: {e}. Skipping invalid value.")
    except TypeError as e:
        print(f"Error: {e}. Skipping invalid value.")
