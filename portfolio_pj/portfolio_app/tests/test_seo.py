from django.test import TestCase, Client


class SeoBatch1Test(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_has_seo_title_description_canonical_and_json_ld(self):
        response = self.client.get("/")
        content = response.content.decode()
        self.assertIn("<title>Duy Nguyen", content)
        self.assertIn('name="description" content="Duy Nguyen designs AI integrations', content)
        self.assertIn('<link rel="canonical" href="https://duynb.com/">', content)
        self.assertIn('property="og:title"', content)
        self.assertIn('"@type": "Person"', content)

    def test_lab_has_seo_title_and_canonical(self):
        response = self.client.get("/lab")
        content = response.content.decode()
        self.assertIn("<title>Lab — Duy Nguyen</title>", content)
        self.assertIn('<link rel="canonical" href="https://duynb.com/lab">', content)
        self.assertNotIn('name="description" content=""', content)

    def test_sitemap_lists_main_pages(self):
        response = self.client.get("/sitemap.xml")
        self.assertEqual(response.status_code, 200)
        content = response.content.decode()
        # In tests the host is testserver; in production the sitemap
        # view builds these from the request host (duynb.com).
        for path in ["/lab</loc>", "/contact</loc>", "/blog</loc>"]:
            self.assertIn(path, content)
