from app_code.person_basic_info import person_basic_info_formatted


def test_person_basic_info_content():
    # Act: Calling the function
    person_case = person_basic_info_formatted()
    # Assert: Check the var type
    assert isinstance(person_case, str)
    # Check if the output matches what is expected
    assert "Full Name:" in person_case
    assert "Gender:" in person_case
    assert "Birth Date:" in person_case
    assert "CPR:" in person_case


def test_cpr_format():
    # Act: Calling the function
    person_case = person_basic_info_formatted()
    # Assert: Check if the CPR is in the correct format (dd/mm/yy-xx)
    assert "CPR:" in person_case
    cpr = person_case.split("CPR: ")[1]
    parts = cpr.split("-")
    assert len(parts) == 2
    # Check dd/mm/yy format after removing the dashes
    assert len(parts[0]) == 6
    assert parts[1].isnumeric()
    # checking cpr length
    assert len(cpr) == 9


def test_gender_match():
    # Arrange: set up the necessary variables to initialize the use case

    # Act: Call the necessary functions
    person_case = person_basic_info_formatted()
    gender = person_case.split('\n')[2].split(': ')[1]  # Extract gender
    cpr = person_case.split('\n')[3].split(': ')[1]  # Extract CPR

    # Assert: checking the gender match:
    assert gender in person_case
    if gender == 'female':
        assert int(cpr[-1]) % 2 == 0  # Check if last digit is even
    elif gender == 'male':
        assert int(cpr[-1]) % 2 != 0  # Check if last digit is odd
