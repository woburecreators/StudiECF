import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="stania_register",
    user="postgres",
    password="9052"
)

def creer_tablefin () :
    cursor = conn.cursor()

    create_table_query = '''
        CREATE TABLE stania_users (
            id SERIAL PRIMARY KEY,
            nom VARCHAR(50) NOT NULL,
            prenom VARCHAR(50) NOT NULL,
            email VARCHAR(100) NOT NULL,
            date_naissance DATE NOT NULL,
            mot_de_passe VARCHAR(50) NOT NULL
        )
    '''
    cursor.execute(create_table_query)
    conn.commit()
    cursor.close()
    conn.close()

creer_tablefin ()