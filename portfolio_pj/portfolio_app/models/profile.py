class Profile:
    def __init__(self, header, profileItems):
        self.header = header
        self.profileItems = profileItems

class ProfileItem:
    def __init__(self, time, title, subTitle, descriptions):
        self.time = time
        self.title = title
        self.subTitle = subTitle
        self.descriptions = descriptions
    
        