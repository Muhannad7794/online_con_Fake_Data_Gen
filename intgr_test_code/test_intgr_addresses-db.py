import pytest
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
