import mysql.connector
from random import choice, randint


def generate_random_address():
    def generate_random_zipCode():
        # Establish the connection
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Cinema77@drama",
            database="addresses"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM postal_code")

        all_codes = cursor.fetchall()
        random_code = choice(all_codes)
        cursor.close()
        connection.close()
        return random_code

    zip_code = generate_random_zipCode()

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'æ', 'ø', 'å']

    def generate_random_street():
        street = ""
        for i in range(5, 15):
            street += choice(alphabet)
        return street

    random_street = generate_random_street()

    def generate_random_street_number():
        street_number = randint(1, 999)
        random_capital_letter = choice(alphabet).upper()
        street_number_specific = f"{street_number}{random_capital_letter}"
        return street_number_specific

    random_street_number = generate_random_street_number()

    def floor_number():
        floor_list = ["st", randint(1, 99)]
        door_credentials = ["tv", "th", "mf"]
        door = choice(door_credentials)
        floor = f"{choice(floor_list)} {door}"
        return floor

    floor = floor_number()

    address = f"{random_street} {random_street_number} {floor}, {zip_code[1]}-{zip_code[0]}".title(
    )
    return address


random_address = generate_random_address()
print(random_address)
