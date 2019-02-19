from .base_context import BaseContext

class BlogsContext(BaseContext):
    def __init__(self,title,blogs,recent_blogs,categories,tags,archives):
        # self.blogs_paginator = blogs_paginator
        self.blogs = blogs
        self.recent_blogs = recent_blogs
        self.categories = categories
        self.tags = tags
        self.archives = archives
        super(BlogsContext,self).__init__(title)

class BlogContext(BaseContext):
    def __init__(self,title,blog,recent_blogs,categories,tags,archives):
        self.blog = blog
        self.recent_blogs = recent_blogs
        self.categories = categories
        self.tags = tags
        self.archives = archives
        super(BlogContext,self).__init__(title)