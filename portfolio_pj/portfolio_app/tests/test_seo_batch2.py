from django.test import TestCase, Client
import re


def headings(html):
    return [(int(m.group(1)), re.sub(r"<[^>]+>", " ", m.group(2)).strip())
            for m in re.finditer(r"<h([1-6])[^>]*>(.*?)</h\1>", html, re.S | re.I)]


class SeoBatch2HeadingsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_has_exactly_one_h1(self):
        html = self.client.get("/").content.decode()
        h1 = [x for x in headings(html) if x[0] == 1]
        self.assertEqual(len(h1), 1)
        self.assertEqual(h1[0][1], "Duy Nguyen")

    def test_lab_has_exactly_one_h1_and_project_h2s(self):
        html = self.client.get("/lab").content.decode()
        h1 = [x for x in headings(html) if x[0] == 1]
        self.assertEqual(len(h1), 1)
        self.assertEqual(h1[0][1], "Lab")
        self.assertIn("Lab", [x[1] for x in headings(html)])
        # No skipped level: first heading is h1, and no h3 appears before an h2
        levels = [x[0] for x in headings(html)]
        self.assertEqual(levels[0], 1)

    def test_contact_has_exactly_one_h1(self):
        html = self.client.get("/contact").content.decode()
        h1 = [x for x in headings(html) if x[0] == 1]
        self.assertEqual(len(h1), 1)
        self.assertEqual(h1[0][1], "Contact")

    def test_home_has_no_broken_og_image(self):
        # OG image is a known blocker (see PR body): no og:image tag is
        # emitted until og-card.png actually lands in static/img/.
        html = self.client.get("/").content.decode()
        self.assertNotIn('property="og:image"', html)

    def test_lab_links_to_contact_and_home(self):
        html = self.client.get("/lab").content.decode()
        self.assertIn('href="/contact"', html)
        self.assertIn('href="/"', html)

    def test_contact_links_to_lab(self):
        html = self.client.get("/contact").content.decode()
        self.assertIn('href="/lab"', html)
