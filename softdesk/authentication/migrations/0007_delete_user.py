# Generated by Django 4.1.7 on 2023-04-04 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_contributors_user_alter_project_author_and_more'),
        ('authentication', '0006_delete_users_user_project'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
