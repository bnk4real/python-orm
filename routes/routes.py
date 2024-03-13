class MainRoute:
    
    def __init__(self, actions):
        self.actions = actions
    
    def routers(self, path, method):
        match path:
            case "/api/test":
                if method == 'GET':
                    return self.actions.routers(path, method)
            case "":
                return "Not found", 404
            case _:
                return "Method not allowed", 405