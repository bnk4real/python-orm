import sqlite3

class Orders:
    def __init__(self, id, customer_id, product, quantity):
        self.id = id
        self.customer_id = customer_id
        self.product = product
        self.quantity = quantity

    def save(self):
        with sqlite3.connect('database/sqlite_customer_test.db') as conn:
            cursor = conn.cursor()

            insert_query = '''
                INSERT INTO tb_orders (id, customer_id, product, quantity)
                VALUES (?, ?, ?, ?)
            '''
            values = (self.id, self.customer_id, self.product, self.quantity)
            cursor.execute(insert_query, values)

            conn.commit()