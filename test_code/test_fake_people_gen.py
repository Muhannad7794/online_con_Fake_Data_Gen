from app_code.fake_people_gen import generate_multiple_fake_persons
from random import randint


def test_generate_multiple_fake_persons():
    # Test valid input
    amount = randint(1, 100)
    result = generate_multiple_fake_persons(amount)
    assert len(result) == amount

    # Test invalid input (TypeError)
    try:
        generate_multiple_fake_persons('not an int')
    except TypeError as e:
        assert str(e) == "number_of_persons must be an integer"

    # Test invalid input (ValueError)
    try:
        generate_multiple_fake_persons(-1)
    except ValueError as e:
        assert str(e) == "number_of_persons must be a positive integer"

    # Test invalid input (ValueError)
    try:
        generate_multiple_fake_persons(101)
    except ValueError as e:
        assert str(e) == "number_of_persons cannot be greater than 100"
