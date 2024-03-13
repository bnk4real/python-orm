import sqlite3

class Users:
    def __init__(self, id:int, fname=str, lname=str, position=str, tel=str, email=str):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.position = position
        self.tel = tel
        self.email = email

    @classmethod
    def get_all(cls):
        with sqlite3.connect('database/sqlite_customer_test.db') as conn:
            cursor = conn.cursor()

            query = 'SELECT id, fname, lname, position, tel, email FROM tb_users ORDER BY id DESC'
            
            cursor.execute(query)
            rows = cursor.fetchall()

            usersList = []
            for row in rows:
                users = cls(*row)
                usersList.append(users)

            return usersList

    def save(self):
        with sqlite3.connect('database/sqlite_customer_test.db') as conn:
            cursor = conn.cursor()

            insert_query = '''
                INSERT INTO tb_users (id, fname, lname, position, tel, email)
                VALUES (?, ?, ?, ?, ?, ?)
            '''
            values = (self.id, self.fname, self.lname, self.position, self.tel, self.email)

            cursor.execute(insert_query, values)

            conn.commit()