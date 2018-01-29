from base_context import BaseContext

class ProfileContext(BaseContext):
    def __init__(self, title, profiles):
        self.title = title
        self.profiles = profiles
        super(ProfileContext,self).__init__(title)

