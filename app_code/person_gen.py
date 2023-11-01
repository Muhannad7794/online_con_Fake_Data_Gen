import pyodbc
import os
from random import choice

def generate_random_person():
    
    if os.environ.get('GITHUB_ACTIONS') == 'true':
        conn_str = 'DRIVER={ODBC Driver 17 for SQL Server};Server=tcp:kea-projects-sql-server.database.windows.net,1433;Database=people;Uid=mual_sql_admin;Pwd=m.u.a.l_KEA_server_access;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
    else:
        server = 'kea-projects-sql-server'
        database = 'addresses_main'
        username = 'mual_sql_admin'
        password = 'm.u.a.l_KEA_server_access'
        conn_str = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:kea-projects-sql-server.database.windows.net,1433;Database=people;Uid=mual_sql_admin;Pwd=m.u.a.l_KEA_server_access;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
    
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM persons')
    all_people = cursor.fetchall()
    random_person = choice(all_people)
    cursor.close()
    conn.close()
    return random_person


# person = generate_random_person()
# print(person)
# print(type(person))

