from repositories.tb_customers import Customers

# input param
deleteCustomer = Customers(
        id = int(input("Enter ID: ")),
    )

# we can validate before execute method
if deleteCustomer.id is None:
    raise ValueError("ID must be provided for deletion.")
elif deleteCustomer.id is not int:
    raise ValueError("Invalid Param: Integer only.")
elif deleteCustomer.id == "":
    raise ValueError("Invalid Param: Param must not empty")

# execute method
deleteCustomer.delete()
print("Customer ID: ", deleteCustomer.id, " was deleted." )