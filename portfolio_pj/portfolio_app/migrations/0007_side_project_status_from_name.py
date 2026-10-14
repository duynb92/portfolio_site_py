from django.db import migrations

STATUS_PREFIXES = {
    '🟢': 'live',
    '🚧': 'in_progress',
}


def move_status_out_of_name(apps, schema_editor):
    # Names carried status as an emoji prefix ("🟢 Coffee Mate"); the status field replaces it
    SideProject = apps.get_model('portfolio_app', 'SideProject')
    for project in SideProject.objects.all():
        for prefix, status in STATUS_PREFIXES.items():
            if project.name.startswith(prefix):
                project.name = project.name[len(prefix):].strip()
                project.status = status
        if project.thumbnail == 'coming-soon.jpg':
            project.thumbnail = ''
        project.save()


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0006_side_project_notebook'),
    ]

    operations = [
        migrations.RunPython(move_status_out_of_name, migrations.RunPython.noop),
    ]
