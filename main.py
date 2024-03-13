# main file should be the file that mainly run the program
# CRUD operation
# from actions.customers import create_customer
# from actions.customers.get_customers import customer
# from actions.customers.update_customer import updated_customer
# from actions.customers.delete_customer import deleteCustomer

import socketserver
from common.constants import PORT

from controllers.controller import MainController
from controllers.get_customers import GetCustomersController

from services.customers.get_customers import GetCustomers

from routes.routes import MainRoute


def main():

    # service
    actions = GetCustomers
    # controller
    main_controller = MainController(actions)
    # route
    main_route = MainRoute(main_controller)

    handler = GetCustomersController(main_route)

    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print("Server started on port", PORT)
        httpd.serve_forever()

if __name__ == "__main__":
    main()