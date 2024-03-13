from common.database.connection import conn, cursor #, execute_query, fetch_rows

# practice to be more well-organized.    

# service in repositories
class Repositories:
    def execute_query(query, values=None):
        if values is None:
            cursor.execute(query)
        else:
            cursor.execute(query, values)
        conn.commit()
    def fetch_rows(query):
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows

# methods in repositories
class Customers:
    def __init__(self, id, fname=None, lname=None, address=None, tel=None, email=None):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.address = address
        self.tel = tel
        self.email = email

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM tb_customers ORDER BY id DESC'
        rows = Repositories.fetch_rows(query)
        customers_list = [cls(*row) for row in rows]
        return customers_list

    def save(self):
        query = '''
            INSERT INTO tb_customers (id, fname, lname, address, tel, email)
            VALUES (?, ?, ?, ?, ?, ?)
        '''
        values = (self.id, self.fname, self.lname, self.address, self.tel, self.email)
        Repositories.execute_query(query, values)

    def update(self):
        query = '''
            UPDATE tb_customers SET fname = ?, lname = ?, address = ?, tel = ?, email = ? WHERE id = ?
        '''
        values = (self.fname, self.lname, self.address, self.tel, self.email, self.id)
        Repositories.execute_query(query, values)

    def delete(self):
        query = 'DELETE FROM tb_customers WHERE id = ?'
        Repositories.execute_query(query, (self.id,))