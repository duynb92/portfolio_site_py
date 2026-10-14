from .base_context import BaseContext

class HomeContext(BaseContext):
    def __init__(self, title, skills, certifications, tools, hobbies):
        self.skills = skills
        self.certifications = certifications
        self.tools = tools
        self.hobbies = hobbies
        super(HomeContext, self).__init__(title)