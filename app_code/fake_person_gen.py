from .person_basic_info import person_basic_info_formatted
from .addresses_gen import generate_random_address
#from .addresses_main_gen import generate_random_address
from .phone_num_gen import generate_random_phone_number


def generate_fake_person():
    basic_info = person_basic_info_formatted()
    address = generate_random_address()
    phone_number = generate_random_phone_number()
    fake_person = f"{basic_info}\nAddress: {address}\nPhone number: {phone_number}"
    return fake_person


# fake_person = generate_fake_person()
# print(fake_person)
