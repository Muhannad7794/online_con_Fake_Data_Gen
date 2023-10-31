import json
from random import choice

# intelize the json file and get the data


def generate_random_person():
    try:
        with open('C:/Muhannad_data/Studying/Projects/Fake_Data_Generator/sorce_data/person-names.json', encoding='utf-8-sig') as persons_data:
            data = json.load(persons_data)
            persons = data['persons']
            random_person = choice(persons)
            surname = random_person['surname']
            name = random_person['name']
            gender = random_person['gender']

    except FileNotFoundError:
        print("File not found, please check the path")
    else:
        return name, surname, gender


# person_1 = generate_random_person()
# print(person_1)
