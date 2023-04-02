# Generated by Django 4.1.7 on 2023-04-02 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_users_projects'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='author',
            field=models.ManyToManyField(blank=True, related_name='projects_author', to='authentication.users'),
        ),
    ]
