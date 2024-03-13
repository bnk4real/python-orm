from repositories.tb_customers import Customers

# Create an instance
create_customer = Customers(
    id = int(input("Enter ID: ")),
    fname = input("Enter Firstname: "),
    lname = input("Enter Lastname: "),
    address = input("Enter Address: "),
    tel = input("Enter Tel: "),
    email = input("Enter Email: "),
)

# save data to the database
create_customer.save()
print("New customer was created.")