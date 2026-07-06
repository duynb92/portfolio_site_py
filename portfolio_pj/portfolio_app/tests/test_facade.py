from django.test import TestCase
from portfolio_app.models.facade import Facade
from portfolio_app.models.project import Project
from portfolio_app.models.skill import Skill
from portfolio_app.models.profile import Profile
from portfolio_app.models.service import Service
from portfolio_app.models.hobby import Hobby
from portfolio_app.models.side_project import SideProject


class FacadeGetProjectsTest(TestCase):
    def setUp(self):
        self.projects = Facade.getProjects()

    def test_returns_list(self):
        self.assertIsInstance(self.projects, list)

    def test_returns_project_instances(self):
        for p in self.projects:
            self.assertIsInstance(p, Project)

    def test_all_projects_have_required_fields(self):
        for p in self.projects:
            self.assertTrue(p.name, msg=f"Project missing name: {p}")
            self.assertTrue(p.tag, msg=f"Project missing tag: {p.name}")
            self.assertTrue(p.filters, msg=f"Project missing filters: {p.name}")
            self.assertIsNotNone(p.categories)
            self.assertIsNotNone(p.links)
            self.assertIsInstance(p.screenshots, int)

    def test_not_empty(self):
        self.assertGreater(len(self.projects), 0)


class FacadeGetSkillsTest(TestCase):
    def setUp(self):
        self.skills = Facade.getSkills()

    def test_returns_list(self):
        self.assertIsInstance(self.skills, list)

    def test_returns_skill_instances(self):
        for s in self.skills:
            self.assertIsInstance(s, Skill)

    def test_all_skills_have_name_and_percent(self):
        for s in self.skills:
            self.assertTrue(s.name)
            self.assertTrue(s.percent)

    def test_percent_ends_with_percent_sign(self):
        for s in self.skills:
            self.assertTrue(s.percent.endswith('%'), msg=f"Skill '{s.name}' percent '{s.percent}' should end with '%'")

    def test_not_empty(self):
        self.assertGreater(len(self.skills), 0)


class FacadeGetProfilesTest(TestCase):
    def setUp(self):
        self.profiles = Facade.getProfiles()

    def test_returns_list(self):
        self.assertIsInstance(self.profiles, list)

    def test_returns_profile_instances(self):
        for p in self.profiles:
            self.assertIsInstance(p, Profile)

    def test_all_profiles_have_header(self):
        for p in self.profiles:
            self.assertTrue(p.header)

    def test_not_empty(self):
        self.assertGreater(len(self.profiles), 0)


class FacadeGetHobbiesTest(TestCase):
    def setUp(self):
        self.hobbies = Facade.getHobbies()

    def test_returns_list(self):
        self.assertIsInstance(self.hobbies, list)

    def test_returns_hobby_instances(self):
        for h in self.hobbies:
            self.assertIsInstance(h, Hobby)

    def test_all_hobbies_have_required_fields(self):
        for h in self.hobbies:
            self.assertTrue(h.name)
            self.assertTrue(h.quote)
            self.assertTrue(h.author)
            self.assertTrue(h.image)

    def test_not_empty(self):
        self.assertGreater(len(self.hobbies), 0)


class FacadeGetServicesTest(TestCase):
    def setUp(self):
        self.services = Facade.getServices()

    def test_returns_list(self):
        self.assertIsInstance(self.services, list)

    def test_returns_service_instances(self):
        for s in self.services:
            self.assertIsInstance(s, Service)

    def test_all_services_have_required_fields(self):
        for s in self.services:
            self.assertTrue(s.name)
            self.assertTrue(s.description)
            self.assertTrue(s.image)

    def test_not_empty(self):
        self.assertGreater(len(self.services), 0)


class FacadeGetSideProjectsTest(TestCase):
    def setUp(self):
        self.side_projects = Facade.getSideProjects()

    def test_returns_list(self):
        self.assertIsInstance(self.side_projects, list)

    def test_returns_side_project_instances(self):
        for sp in self.side_projects:
            self.assertIsInstance(sp, SideProject)

    def test_all_side_projects_have_required_fields(self):
        for sp in self.side_projects:
            self.assertTrue(sp.name)
            self.assertTrue(sp.thumbnail)
            self.assertIsInstance(sp.tech_tags, list)

    def test_not_empty(self):
        self.assertGreater(len(self.side_projects), 0)
