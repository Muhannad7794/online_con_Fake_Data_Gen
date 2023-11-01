import pyodbc
from app_code.person_gen import generate_random_person


def test_generate_random_person():
    # Arrange: No specific setup required for this function

    # Act: Call the function
    result = generate_random_person()

    # Assert: Check the result
    assert isinstance(result, pyodbc.Row)
    assert len(result) == 3
    assert isinstance(result[0], str)
    assert isinstance(result[1], str)
    assert isinstance(result[2], str)
