def get_db_connection():
    return psycopg2.connect(
        dbname="mbarreras_db",
        user="mbarreras",
        password="B133eras",
        host="localhost",
        port="5432"
    )