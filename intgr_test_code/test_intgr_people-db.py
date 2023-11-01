import pyodbc
import os

def test_integration_generate_random_person():
    if os.environ.get('GITHUB_ACTIONS') == 'true':
        conn_str = 'DRIVER={ODBC Driver 17 for SQL Server};Server=tcp:kea-projects-sql-server.database.windows.net,1433;Database=people;Uid=mual_sql_admin;Pwd=m.u.a.l_KEA_server_access;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
    else:
        try:
            # Arrange: Set up connection parameters
            server = 'your_server_name'
            database = 'your_database_name'
            username = 'your_username'
            password = 'your_password'
            conn_str = f'Driver={{ODBC Driver 18 for SQL Server}};' \
                    f'Server=tcp:kea-projects-sql-server.database.windows.net;' \
                    f'Database=people;Uid=mual_sql_admin;Pwd=m.u.a.l_KEA_server_access;' \
                    f'Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'

            # Act: Test connection and data retrieval
            with pyodbc.connect(conn_str) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM persons')  

                # Assert: Verify data retrieval
                rows = cursor.fetchall()
                assert len(rows) > 0  # Check if data was retrieved

        except pyodbc.Error as e:
            # If an exception occurs, handle it here
            assert False, f'Error: {e}'

        except Exception as e:
            # Handle any other exceptions here
            assert False, f'Error: {e}'
