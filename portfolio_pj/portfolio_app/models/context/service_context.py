from base_context import BaseContext

class ServiceContext(BaseContext):
    services = []
    def __init__(self, title, services):
        self.services = services
        super(ServiceContext, self).__init__(title)