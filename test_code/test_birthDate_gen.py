from app_code.birthDate_gen import generate_random_birthdate


def test_generate_random_birthdate():
    # Arrange: No specific setup required for this function

    # Act: Call the function
    result = generate_random_birthdate()

    # Assert: Check the result
    assert isinstance(result, str)
    assert len(result) == 8
    assert result[:2].isnumeric() and 1 <= int(result[:2]) <= 28
    assert result[3:5].isnumeric() and 1 <= int(result[3:5]) <= 12
    assert result[6:].isnumeric() and 0 <= int(result[6:]) <= 99
