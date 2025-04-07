def get_db_connection():
    return psycopg2.connect(
        dbname="mbarreras_db",
        user="**********",
        password="*********",
        host="localhost",
        port="5432"
    )