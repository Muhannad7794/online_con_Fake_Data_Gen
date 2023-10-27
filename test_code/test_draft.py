# from app_code.person_basic_info import person_basic_info_formatted


# def test_person_basic_info_content():

#     # Act: Calling the function
#     result = person_basic_info_formatted()
#     # Assert: Check the result
#     assert isinstance(result, str)

#     # Check if the expected fields are present in the result
#     assert "Name:" in result
#     assert "Surname:" in result
#     assert "Gender:" in result
#     assert "Birth date:" in result
#     assert "CPR:" in result


# def test_gender_matching_when_male():
#     # Arrange: Generate random person and birth date for testing
#     person_case = ('Mimir S.', 'Krogh', 'male')
#     birth_day = '05/09/90'  # Example birth date (in dd/mm/yy format)

#     # Act: Call the function
#     create_person = person_basic_info_formatted()

#     # Assert: Check if the Gender in the output matches the input to generate_random_cpr
#     assert person_case[2] in create_person
#     assert person_case[2] == 'male'


# def test_person_basic_info_cpr_format():
#     # Arrange: Generate random person and birth date for testing
#     person = ('Mimir S.', 'Krogh', 'male')
#     birth_day = '05/09/90'  # Example birth date (in dd/mm/yy format)

#     # Act: Call the function
#     result = person_basic_info_formatted()

#     # Assert: Check if the CPR is in the correct format (dd/mm/yy-xx)
#     assert "CPR:" in result
#     cpr = result.split("CPR: ")[1]
#     parts = cpr.split("-")
#     assert len(parts) == 2
#     assert len(parts[0]) == 8  # Check dd/mm/yy format and counting the dashes
#     assert parts[1].isnumeric()


# # def test_person_basic_info_cpr_matching_birthdate():
# #     # Arrange: Generate random person and birth date for testing
# #     person = ('Mimir S.', 'Krogh', 'male')
# #     birth_day = '05/09/90'  # Example birth date (in dd/mm/yy format)

# #     # Act: Call the function
# #     result = person_basic_info_formatted()

# #     # Assert: Check if the CPR digits are matching the digits from the birthdate
# #     assert f'Birth date: {birth_day}' in result
# #     birth_date_parts = birth_day.split("/")
# #     cpr = result.split("CPR: ")[1]
# #     cpr_date = cpr.split("-")[0]
# #     assert cpr_date == birth_date_parts[0] + \
# #         birth_date_parts[1] + birth_date_parts[2][-2:]


# # def test_person_basic_info_last_two_digits_even_odd():
# #     # Arrange: Generate random person and birth date for testing
# #     person = ('Mimir S.', 'Krogh', 'male')
# #     birth_day = '05/09/90'  # Example birth date (in dd/mm/yy format)

# #     # Act: Call the function
# #     result = person_basic_info_formatted()

# #     # Assert: Check if the last two digits in the CPR construct an even number if the gender is female
# #     # and an odd number if the gender is male
# #     cpr = result.split("CPR: ")[1]
# #     last_two_digits = int(cpr.split("-")[1])
# #     if person[2] == 'female':
# #         assert last_two_digits % 2 == 0
# #     elif person[2] == 'male':
# #         assert last_two_digits % 2 != 0
