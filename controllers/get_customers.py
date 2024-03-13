import http.server

def GetCustomersController(main_route):
    class GetCustomersHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            response = main_route.routers(self.path, self.command)
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(response.encode('utf-8'))
    return GetCustomersHandler