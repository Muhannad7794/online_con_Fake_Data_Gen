from app_code.CPR_gen import generate_random_cpr
import sys
sys.path.insert(
    0, 'C:/Muhannad_data/Studying/Projects/Fake_Data_Generator/app_code')


def test_cpr_type():
    # Arrange: Generate random person and birth date for testing
    # # Act: Call the function
    cpr = generate_random_cpr()
    # Assert: Check the cpr
    assert isinstance(cpr, list)
    assert len(cpr) == 3


def test_verify_birthDate_cpr_reletivity():
    profile = generate_random_cpr()
    birth_date = profile[1]
    cpr = profile[2]
    assert cpr[:6] == birth_date.replace('/', '')


def test_gender_match():
    profile = generate_random_cpr()
    gender = profile[0][2]
    cpr = profile[2]
    if gender == 'female':
        assert int(cpr[7:9]) % 2 == 0

    elif gender == 'male':
        assert int(cpr[7:9]) % 2 != 0
