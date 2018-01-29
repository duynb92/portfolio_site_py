class Project:
    def __init__(self, name, tag, description, client, roles, skills, length, categories, links, screenshots):
        self.name = name
        self.tag = tag
        self.description = description
        self.client = client
        self.roles = roles
        self.skills = skills
        self.length = length
        self.categories = categories
        self.links = links
        self.screenshots = screenshots

class Link:
    def __init__(self, url, platform):
        self.url = url
        self.platform = platform

class Category:
    MOBILE = 1
    WEB = 2
    DESKTOP = 3
    LINUX = 4

class Platform:
    IOS = 1
    ANDROID = 2
    WEB = 3
    WINDOWS = 4