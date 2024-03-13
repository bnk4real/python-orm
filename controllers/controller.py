# controllers/main_controller.py
class MainController:
    def __init__(self, main_service):
        self.main_service = main_service
    
    def routers(self, path, method):
        return self.main_service.GetAll(self)