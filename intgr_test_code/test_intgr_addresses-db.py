import pyodbc
from app_code.addresses_main_gen import generate_random_address

def test_database_interaction():
    # Define your connection parameters
    server = 'kea-projects-sql-server'
    database = 'addresses_main'
    username = 'mual_sql_admin'
    password = 'm.u.a.l_KEA_server_access'
    driver = '{ODBC Driver 18 for SQL Server}'
    conn_str = 'DRIVER={ODBC Driver 18 for SQL Server};Server=tcp:kea-projects-sql-server.database.windows.net,1433;Database=addresses_main;Uid=mual_sql_admin;Pwd=m.u.a.l_KEA_server_access;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'

    # Establish a connection
    conn = pyodbc.connect(conn_str)

    # Create a cursor from the connection
    cursor = conn.cursor()

    # Execute SQL queries
    cursor.execute('SELECT * FROM postal_code')

    # Fetch rows from the last executed query
    all_codes = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Now, use the generate_random_address function
    address = generate_random_address()

    # Add your assertions based on the expected behavior
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
    assert len(all_codes) > 0
    
