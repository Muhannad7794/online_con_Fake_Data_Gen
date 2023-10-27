from app_code.fake_person_gen import generate_fake_person


def test_fake_person_gen():
    person = generate_fake_person()
    assert person is not None
    assert len(person) > 0
    assert "Full Name:" in person
    assert "Gender:" in person
    assert "Birth Date:" in person
    assert "CPR:" in person
    assert "Address:" in person
    assert "Phone number:" in person
    # checking that the CPR is constructed from the numbers in the Birth Date:
    cpr = person.split("CPR: ")[1].split("\n")[0]
    birth_date = person.split("Birth Date: ")[1].split("\n")[0]
    assert birth_date.replace("/", "") in cpr
    # hecking if the last digit of the CPR after '-' is even when gender == 'female' and odd when gender == 'male':
    gender = person.split("Gender: ")[1].split("\n")[0]
    cpr_last_digit = int(cpr.split("-")[1])
    if gender == 'female':
        assert cpr_last_digit % 2 == 0
    elif gender == 'male':
        assert cpr_last_digit % 2 == 1
