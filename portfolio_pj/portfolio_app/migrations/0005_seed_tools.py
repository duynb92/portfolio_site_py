import uuid
from django.db import migrations


def seed_tools(apps, schema_editor):
    Tool = apps.get_model('portfolio_app', 'Tool')
    cdn = "https://cdn.jsdelivr.net/gh/glincker/thesvg@main/public/icons/{}/default.svg"
    tools_data = [
        ("Claude Code", "claude-code", "https://www.anthropic.com/claude-code"),
        ("GitHub", "github", "https://github.com/duynb92"),
        ("AWS", "aws", "https://aws.amazon.com"),
        ("Google Cloud", "google-cloud", "https://cloud.google.com"),
        ("Docker", "docker", "https://www.docker.com"),
    ]
    for i, (name, slug, link) in enumerate(tools_data):
        Tool.objects.create(id=uuid.uuid4(), name=name, icon=cdn.format(slug), link=link, order=i)


def remove_tools(apps, schema_editor):
    apps.get_model('portfolio_app', 'Tool').objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0004_tool'),
    ]

    operations = [
        migrations.RunPython(seed_tools, remove_tools),
    ]
