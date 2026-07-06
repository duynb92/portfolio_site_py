from django.test import TestCase, Client
from django.utils import timezone
from portfolio_app.models.blog import Blog, Tag, Category


def make_category(title="Tech"):
    return Category.objects.create(title=title)


def make_tag(title="python"):
    return Tag.objects.create(title=title)


def make_blog(title="Test Blog", category=None, pub_date=None):
    if category is None:
        category = make_category()
    if pub_date is None:
        pub_date = timezone.datetime(2024, 6, 15, 12, 0, 0, tzinfo=timezone.utc)
    return Blog.objects.create(
        title=title,
        content="<p>Content</p>",
        pub_date=pub_date,
        category=category,
    )


class StaticPageViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_returns_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')

    def test_index_context_has_skills_and_hobbies(self):
        response = self.client.get('/')
        context = response.context['context']
        self.assertTrue(hasattr(context, 'skills'))
        self.assertTrue(hasattr(context, 'hobbies'))

    def test_profile_returns_200(self):
        response = self.client.get('/profile')
        self.assertEqual(response.status_code, 200)

    def test_profile_uses_correct_template(self):
        response = self.client.get('/profile')
        self.assertTemplateUsed(response, 'profile.html')

    def test_service_returns_200(self):
        response = self.client.get('/services')
        self.assertEqual(response.status_code, 200)

    def test_service_uses_correct_template(self):
        response = self.client.get('/services')
        self.assertTemplateUsed(response, 'services.html')

    def test_lab_returns_200(self):
        response = self.client.get('/lab')
        self.assertEqual(response.status_code, 200)

    def test_lab_uses_correct_template(self):
        response = self.client.get('/lab')
        self.assertTemplateUsed(response, 'lab.html')

    def test_contact_returns_200(self):
        response = self.client.get('/contact')
        self.assertEqual(response.status_code, 200)

    def test_contact_uses_correct_template(self):
        response = self.client.get('/contact')
        self.assertTemplateUsed(response, 'contact-3.html')


class BlogListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = make_category()
        for i in range(3):
            make_blog(title=f"Blog {i}", category=self.category)

    def test_blog_list_returns_200(self):
        response = self.client.get('/blog')
        self.assertEqual(response.status_code, 200)

    def test_blog_list_uses_correct_template(self):
        response = self.client.get('/blog')
        self.assertTemplateUsed(response, 'blog-list.html')

    def test_blog_list_context_has_expected_keys(self):
        response = self.client.get('/blog')
        context = response.context['context']
        self.assertTrue(hasattr(context, 'blogs'))
        self.assertTrue(hasattr(context, 'recent_blogs'))
        self.assertTrue(hasattr(context, 'categories'))
        self.assertTrue(hasattr(context, 'tags'))
        self.assertTrue(hasattr(context, 'archives'))


class BlogDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.blog = make_blog()

    def test_blog_detail_get_returns_200(self):
        url = f'/blog/2024/6/15/{self.blog.slug}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_blog_detail_uses_correct_template(self):
        url = f'/blog/2024/6/15/{self.blog.slug}'
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'blog-details.html')

    def test_blog_detail_post_valid_comment_redirects(self):
        url = f'/blog/2024/6/15/{self.blog.slug}'
        response = self.client.post(url, {
            'name': 'Alice',
            'email': 'alice@example.com',
            'content': 'Great post!',
            'parent': '',
        })
        self.assertEqual(response.status_code, 302)

    def test_blog_detail_post_invalid_comment_rerenders(self):
        url = f'/blog/2024/6/15/{self.blog.slug}'
        response = self.client.post(url, {'name': '', 'email': 'bad', 'content': ''})
        self.assertEqual(response.status_code, 200)


class BlogArchiveViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        make_blog()

    def test_archive_returns_200(self):
        response = self.client.get('/blog/2024/6')
        self.assertEqual(response.status_code, 200)

    def test_archive_uses_blog_list_template(self):
        response = self.client.get('/blog/2024/6')
        self.assertTemplateUsed(response, 'blog-list.html')


class BlogTagViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.tag = make_tag()
        blog = make_blog()
        blog.tags.add(self.tag)

    def test_tag_view_returns_200(self):
        response = self.client.get(f'/blog/tag/{self.tag.slug}')
        self.assertEqual(response.status_code, 200)

    def test_tag_view_uses_blog_list_template(self):
        response = self.client.get(f'/blog/tag/{self.tag.slug}')
        self.assertTemplateUsed(response, 'blog-list.html')


class BlogCategoryViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = make_category()
        make_blog(category=self.category)

    def test_category_view_returns_200(self):
        response = self.client.get(f'/blog/category/{self.category.slug}')
        self.assertEqual(response.status_code, 200)

    def test_category_view_uses_blog_list_template(self):
        response = self.client.get(f'/blog/category/{self.category.slug}')
        self.assertTemplateUsed(response, 'blog-list.html')


class GetBlogsWithPagingTest(TestCase):
    def setUp(self):
        self.client = Client()
        category = make_category()
        for i in range(12):
            make_blog(title=f"Blog {i}", category=category)

    def test_first_page_has_5_items(self):
        response = self.client.get('/blog?page=1')
        blogs = response.context['context'].blogs
        self.assertEqual(len(blogs), 5)

    def test_invalid_page_falls_back_to_page_1(self):
        response = self.client.get('/blog?page=notanumber')
        blogs = response.context['context'].blogs
        self.assertEqual(blogs.number, 1)

    def test_page_beyond_last_returns_last_page(self):
        response = self.client.get('/blog?page=999')
        blogs = response.context['context'].blogs
        self.assertEqual(blogs.number, blogs.paginator.num_pages)
