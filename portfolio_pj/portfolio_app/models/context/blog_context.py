from .base_context import BaseContext

class BlogContext(BaseContext):
    def __init__(self,title,blogs,recent_blogs,categories,tags,archives):
        self.blogs = blogs
        self.recent_blogs = recent_blogs
        self.categories = categories
        self.tags = tags
        self.archives = archives
        super(BlogContext,self).__init__(title)

class BlogDetailContext(BaseContext):
    def __init__(self,title,blog,recent_blogs,categories,tags,archives):
        self.blog = blog
        self.recent_blogs = recent_blogs
        self.categories = categories
        self.tags = tags
        self.archives = archives
        super(BlogDetailContext,self).__init__(title)