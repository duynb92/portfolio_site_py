class BaseContext(object):
    def __init__(self, title, seo_title=None, seo_description=None):
        self.title = title
        # Per-page SEO metadata. Views set these explicitly; templates
        # fall back to a generic title/description when they are absent,
        # so older contexts keep working unchanged.
        self.seo_title = seo_title
        self.seo_description = seo_description