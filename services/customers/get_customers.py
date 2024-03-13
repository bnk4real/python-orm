from repositories.tb_customers import Customers
import json

class GetCustomers:
    def GetAll(self):
        getall = Customers.get_all()
        data = []
        for customer in getall:
            cust_data = {
                "ID": customer.id,
                "Name": customer.fname,
                "Latname": customer.lname,
                "Address": customer.address,
                "Tel": customer.tel,
                "Email": customer.email
            }
            data.append(cust_data)

        resp = json.dumps(data)
        return resp