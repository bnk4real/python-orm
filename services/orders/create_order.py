from repositories.tb_orders import Orders

# Create an instance of Orders class with the data you want to update
orders = Orders(
    id = 2, 
    customer_id = 4, 
    product = 'Acer', 
    quantity = 3, 
)

# Call the update method to update the customer's data
orders.save()
print("New order created.")