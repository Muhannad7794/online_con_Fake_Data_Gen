import json
from app_code.person_gen import generate_random_person
import os

def test_json_interaction():
    json_path = os.getenv('JSON_PATH_GITHUB')

    if json_path:
        file_path = os.path.join(json_path, 'person-names.json')
    else:
        file_path = 'C:\\Muhannad_data\\Studying\\Projects\\Fake_Data_Generator\\sorce_data\\person-names.json'
        
    try:
        with open(file_path, encoding='utf-8-sig') as persons_data:
            data = json.load(persons_data)
            persons = data['persons']
            random_person = generate_random_person()

            # Add your assertions based on the expected behavior
            assert isinstance(random_person, tuple)
            assert len(random_person) == 3
            assert isinstance(random_person[0], str)
            assert isinstance(random_person[1], str)
            assert isinstance(random_person[2], str)

    except FileNotFoundError:
        print("File not found, please check the path")
        assert False  # Fail the test if the file is not found
