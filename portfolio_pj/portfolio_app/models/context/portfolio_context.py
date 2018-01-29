from base_context import BaseContext
from ..project import *

class PortfolioContext(BaseContext):
    def __init__(self, title, projects):
        self.projects = projects
        super(PortfolioContext, self).__init__(title)