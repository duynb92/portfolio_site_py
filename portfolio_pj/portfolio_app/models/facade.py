from django.db.models import Prefetch
from .skill import Skill
from .certification import Certification
from .hobby import Hobby
from .service import Service
from .side_project import SideProject
from .profile import Profile, ProfileItem
from .project import Project


class Facade:
    @staticmethod
    def getProjects():
        return list(Project.objects.prefetch_related('link_set').all())

    @staticmethod
    def getSkills():
        return list(Skill.objects.all())

    @staticmethod
    def getProfiles():
        active_items = Prefetch(
            'items',
            queryset=ProfileItem.objects.filter(is_active=True),
            to_attr='active_items',
        )
        return list(Profile.objects.prefetch_related(active_items).all())

    @staticmethod
    def getHobbies():
        return list(Hobby.objects.all())

    @staticmethod
    def getSideProjects():
        return list(SideProject.objects.all())

    @staticmethod
    def getCertifications():
        return list(Certification.objects.all())

    @staticmethod
    def getServices():
        return list(Service.objects.all())
