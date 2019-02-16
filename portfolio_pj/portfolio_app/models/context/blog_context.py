from .base_context import BaseContext

class BlogContext(BaseContext):
    def __init__(self,title,blogs):
        self.blogs = blogs
        super(BlogContext,self).__init__(title)

class BlogDetailContext(BaseContext):
    def __init__(self,title,blog):
        self.blog = blog
        super(BlogDetailContext,self).__init__(title)