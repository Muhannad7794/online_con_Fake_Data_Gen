import pyodbc
from random import choice, randint


def generate_random_address():
    def generate_random_zipCode():
        # Define the connection string
        server = 'kea-projects-sql-server'
        database = 'addresses_main'
        username = 'mual_sql_admin'
        password = 'm.u.a.l_KEA_server_access'
        # Use the appropriate driver
        driver = '{ODBC Driver 18 for SQL Server}'

        # Create the connection string
        conn_str = 'DRIVER={ODBC Driver 18 for SQL Server};Server=tcp:kea-projects-sql-server.database.windows.net,1433;Database=addresses_main;Uid=mual_sql_admin;Pwd=m.u.a.l_KEA_server_access;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'

        # Establish the connection
        conn = pyodbc.connect(conn_str)

        # Create a cursor from the connection
        cursor = conn.cursor()

        # Now you can execute SQL queries
        # Replace with your actual table name
        cursor.execute('SELECT * FROM postal_code')

        # Fetch rows from the last executed query
        all_codes = cursor.fetchall()
        random_code = choice(all_codes)
        cursor.close()
        conn.close()
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


# random_address = generate_random_address()
# print(random_address)
