import json
from .base_context import BaseContext

class HomeContext(BaseContext):
    def __init__(self, title, skills, certifications, tools, hobbies, hero_roles):
        self.skills = skills
        self.certifications = certifications
        self.tools = tools
        self.hobbies = hobbies
        self.hero_roles = [role.text for role in hero_roles]
        super(HomeContext, self).__init__(title)

    @property
    def hero_roles_json(self):
        return json.dumps(self.hero_roles)
