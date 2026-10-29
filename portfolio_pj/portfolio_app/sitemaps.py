from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticSitemap(Sitemap):
    """Main public pages only. Blog detail URLs are left out of Batch 1:
    the internal blog list links out to Medium and the detail pages are
    legacy content, so they get canonical/meta tags but no sitemap entry
    until the blog alignment work in a later batch."""

    changefreq = "weekly"

    def items(self):
        return ["index", "lab", "contact", "blog", "profile", "service"]

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        return 1.0 if item == "index" else 0.8
