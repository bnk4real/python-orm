from repositories.tb_users import Users

customer = Users(
    id = 3, 
    fname = 'Pipe', 
    lname = 'Meena', 
    position = 'Marketing', 
    tel = '564-4567', 
    email = 'pip@example.com'
)

customer.save()
print("New user created.")