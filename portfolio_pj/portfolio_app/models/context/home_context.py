from base_context import BaseContext

class HomeContext(BaseContext):
    def __init__(self,title, skills, hobbies):
        self.skills = skills
        self.hobbies = hobbies
        super(HomeContext,self).__init__(title)