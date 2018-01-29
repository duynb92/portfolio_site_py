from context.base_context import BaseContext

class Portfolio(BaseContext):
    def __init__(self, name, description):
        self.name = name
        self.description = description