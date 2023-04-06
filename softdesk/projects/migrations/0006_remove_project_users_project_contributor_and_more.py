# Generated by Django 4.1.7 on 2023-04-06 16:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0005_contributor_delete_contributors_alter_project_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='users',
        ),
        migrations.AddField(
            model_name='project',
            name='contributor',
            field=models.ManyToManyField(null=True, related_name='contributor_project', through='projects.Contributor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='contributor',
            unique_together={('user', 'project')},
        ),
    ]
