import sqlite3

with sqlite3.connect('common/database/sqlite_customer_test.db') as conn:
    try:
        cursor = conn.cursor()
    except sqlite3.Error as err:
        print("connection error: ", err)