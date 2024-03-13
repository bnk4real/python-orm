from repositories.tb_users import Users

# Retrieve all customers
getall = Users.get_all()

# Print the retrieved data
for user in getall:
    print(f"ID: {user.id}, Name: {user.fname} {user.lname}, Position: {user.position}")