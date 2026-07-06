from django.test import TestCase
from django.utils import timezone
from portfolio_app.models.blog import Blog, BlogComment, Tag, Category


def make_category(title="Tech"):
    return Category.objects.create(title=title)


def make_blog(title="Test Blog", content="<p>Hello <b>world</b></p>", category=None):
    if category is None:
        category = make_category()
    return Blog.objects.create(
        title=title,
        content=content,
        pub_date=timezone.datetime(2024, 6, 15, 12, 0, 0, tzinfo=timezone.utc),
        category=category,
    )


class BlogGetPreviewTest(TestCase):
    def test_strips_html_tags(self):
        blog = make_blog(content="<p>Hello <b>world</b></p>" * 20)
        preview = blog.getPreview()
        self.assertNotIn('<p>', preview)
        self.assertNotIn('<b>', preview)

    def test_truncates_to_300_chars_plus_ellipsis(self):
        blog = make_blog(content="a" * 500)
        preview = blog.getPreview()
        self.assertTrue(preview.endswith("..."))
        self.assertEqual(len(preview), 303)

    def test_short_content_still_appends_ellipsis(self):
        blog = make_blog(content="Short")
        preview = blog.getPreview()
        self.assertTrue(preview.endswith("..."))


class BlogDateHelpersTest(TestCase):
    def setUp(self):
        self.blog = make_blog()

    def test_getDateTime_format(self):
        self.assertEqual(self.blog.getDateTime(), "15, June, 2024")

    def test_getDateOnly(self):
        self.assertEqual(self.blog.getDateOnly(), "15")

    def test_getMonthOnly(self):
        self.assertEqual(self.blog.getMonthOnly(), "Jun")

    def test_getMonth(self):
        self.assertEqual(self.blog.getMonth(), "06")

    def test_getYearOnly(self):
        self.assertEqual(self.blog.getYearOnly(), "2024")


class BlogGetFirstImageUrlTest(TestCase):
    def test_returns_url_when_image_present(self):
        content = '<p><img src="https://example.com/img.png" /></p>'
        blog = make_blog(content=content)
        url = blog.getFirstImageUrl()
        self.assertIsNotNone(url)
        self.assertIn("example.com", url)

    def test_returns_none_when_no_image(self):
        blog = make_blog(content="<p>No image here</p>")
        self.assertIsNone(blog.getFirstImageUrl())


class BlogRemoveTagsTest(TestCase):
    def test_removes_simple_tags(self):
        blog = make_blog()
        self.assertEqual(blog.remove_tags("<p>hello</p>"), "hello")

    def test_removes_nested_tags(self):
        blog = make_blog()
        self.assertEqual(blog.remove_tags("<div><span>text</span></div>"), "text")

    def test_leaves_plain_text_unchanged(self):
        blog = make_blog()
        self.assertEqual(blog.remove_tags("plain text"), "plain text")


class BlogGetArchivesTest(TestCase):
    def test_returns_dict(self):
        make_blog()
        archives = Blog.getArchives()
        self.assertIsInstance(archives, dict)

    def test_year_keys_contain_month_lists(self):
        make_blog()
        archives = Blog.getArchives()
        for year, months in archives.items():
            self.assertIsInstance(months, list)
            self.assertGreater(len(months), 0)

    def test_no_duplicate_months_per_year(self):
        category = make_category()
        Blog.objects.create(
            title="Blog 1",
            content="content",
            pub_date=timezone.datetime(2024, 6, 1, tzinfo=timezone.utc),
            category=category,
        )
        Blog.objects.create(
            title="Blog 2",
            content="content",
            pub_date=timezone.datetime(2024, 6, 15, tzinfo=timezone.utc),
            category=category,
        )
        archives = Blog.getArchives()
        months = archives.get("2024", [])
        self.assertEqual(len(months), len(set(months)))

    def test_empty_db_returns_empty_dict(self):
        archives = Blog.getArchives()
        self.assertEqual(archives, {})


class BlogCommentIsParentTest(TestCase):
    def setUp(self):
        self.blog = make_blog()

    def test_comment_without_parent_is_parent(self):
        comment = BlogComment.objects.create(
            name="Alice",
            email="alice@example.com",
            content="Top level",
            blog=self.blog,
        )
        self.assertTrue(comment.isParent)

    def test_comment_with_parent_is_not_parent(self):
        parent = BlogComment.objects.create(
            name="Alice",
            email="alice@example.com",
            content="Top level",
            blog=self.blog,
        )
        reply = BlogComment.objects.create(
            name="Bob",
            email="bob@example.com",
            content="Reply",
            parent=parent,
            blog=self.blog,
        )
        self.assertFalse(reply.isParent)
