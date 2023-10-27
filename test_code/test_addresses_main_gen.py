# test_addresses_main_gen.py

from app_code.addresses_main_gen import generate_random_address


def test_generate_random_address():
    address = generate_random_address()
    assert isinstance(address, str)
    assert address.istitle()
    assert len(address) > 0
    address_as_list = address.split()
    assert isinstance(address_as_list, list)
    assert len(address_as_list) == 5 or len(address_as_list) == 6
    assert address_as_list[0].istitle()
    assert isinstance(address_as_list[1], str)
    assert isinstance(address_as_list[2], str)
    assert address_as_list[3].istitle()
    assert isinstance(address_as_list[4], str)


# def test_generate_random_zipCode():
#     zip_code = generate_random_zipCode()
#     assert isinstance(zip_code, tuple)
#     assert len(zip_code) == 2


# def test_generate_random_street():
#     address = generate_random_street()
#     assert isinstance(address, str)
#     assert len(address) >= 5 and len(address) <= 15


# def test_generate_random_street_number():
#     address = generate_random_street_number()
#     assert isinstance(address, str)
#     assert address[:-1].isdigit()
#     assert address[-1].isalpha() and address[-1].isupper()


# def test_floor_number():
#     address = floor_number()
#     assert isinstance(address, str)
#     assert address in ["st tv", "st th", "st mf"] or address.isdigit()
