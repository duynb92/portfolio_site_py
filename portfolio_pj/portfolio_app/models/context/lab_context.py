from .base_context import BaseContext

class LabContext(BaseContext):
    side_projects = []
    def __init__(self, title, side_projects):
        self.side_projects = side_projects
        super(LabContext, self).__init__(title)
