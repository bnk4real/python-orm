from repositories.tb_customers import Customers

# Create an instance of Customers class with the data you want to update
# updated_customer = Customers(
#     id = 4,
#     fname = 'Marvin',
#     lname = 'Milin',
#     address = '789 Block D.',
#     tel = '356-4321',
#     email = 'marvinb@email.com'
# )

updated_customer = Customers(
    id = int(input("Enter ID: ")),
    fname = input("Enter Firstname: "),
    lname = input("Enter Lastname: "),
    address = input("Enter Address: "),
    tel = input("Enter Tel: "),
    email = input("Enter Email: "),
)


# Call the update method to update the customer's data
updated_customer.update()
print("Customer Data updated.")