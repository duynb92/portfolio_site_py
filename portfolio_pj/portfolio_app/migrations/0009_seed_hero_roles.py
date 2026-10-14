import uuid
from django.db import migrations


def seed_hero_roles(apps, schema_editor):
    HeroRole = apps.get_model('portfolio_app', 'HeroRole')
    roles = ["Senior Software Engineer", "Claude & AWS & Google Certified"]
    for i, text in enumerate(roles):
        HeroRole.objects.create(id=uuid.uuid4(), text=text, order=i)


def remove_hero_roles(apps, schema_editor):
    apps.get_model('portfolio_app', 'HeroRole').objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0008_hero_role'),
    ]

    operations = [
        migrations.RunPython(seed_hero_roles, remove_hero_roles),
    ]
