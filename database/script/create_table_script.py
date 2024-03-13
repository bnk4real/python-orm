import sqlite3

def create_tables():
    conn = sqlite3.connect('database/sqlite_customer_test.db')  # Specify the path to the database
    cursor = conn.cursor()

    create_table_queries = [
        '''
        CREATE TABLE IF NOT EXISTS tb_customers (
            id INTEGER PRIMARY KEY,
            fname TEXT,
            lname TEXT,
            address TEXT,
            tel TEXT,
            email TEXT
        )
        ''',
        '''
        CREATE TABLE IF NOT EXISTS tb_users (
            id INTEGER PRIMARY KEY,
            fname TEXT,
            lname TEXT,
            position TEXT,
            tel TEXT,
            email TEXT
        )
        ''',
        '''
        CREATE TABLE IF NOT EXISTS tb_orders (
            id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            product TEXT,
            quantity INTEGER,
            FOREIGN KEY (customer_id) REFERENCES tb_customers (id)
        )
        '''
    ]
	# example only

    for query in create_table_queries:
        cursor.execute(query)

    conn.commit()
    print("Create tables successfully.")
    conn.close()

if __name__ == "__main__":
    create_tables()