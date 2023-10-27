from app_code.phone_num_gen import generate_random_phone_number


def test_phone_number_structure():
    phone_number = generate_random_phone_number()
    starter, num_tail = phone_number.split('-')[1:]
    # Check if starter and num_tail are numeric
    assert starter.isnumeric()
    assert num_tail.isnumeric()
    # Check if the structure is correct
    assert phone_number.startswith("+45")
    assert phone_number[3] == "-"


def test_phone_number_length():
    phone_number = generate_random_phone_number()
    assert len(phone_number) == 13


def test_num_tail_length():
    phone_number = generate_random_phone_number()
    starter, num_tail = phone_number.split('-')[1:]
    if len(starter) == 1:
        assert len(num_tail) == 7
    elif len(starter) == 2:
        assert len(num_tail) == 6
    elif len(starter) == 3:
        assert len(num_tail) == 5
    elif len(starter) == 4:
        assert len(num_tail) == 4
    elif len(starter) == 5:
        assert len(num_tail) == 3
    elif len(starter) == 6:
        assert len(num_tail) == 2
    elif len(starter) > 7:
        assert generate_random_phone_number() == "Starter is too long"
