# Generated by Django 4.1.7 on 2023-04-06 18:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(choices=[('Admin', 'Admin'), ('list', 'List'), ('Delete', 'Delete'), ('Update', 'Update')], default='Admin', max_length=15)),
                ('role', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=5000)),
                ('type', models.CharField(choices=[('Back-end', 'Back End'), ('Front-end', 'Front End'), ('IOS', 'Ios'), ('Android', 'Android')], default='Back-end', max_length=15)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_author', to=settings.AUTH_USER_MODEL)),
                ('contributor', models.ManyToManyField(null=True, related_name='contributor_project', through='project.Contributor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=5000)),
                ('tag', models.CharField(choices=[('Bug', 'Bug'), ('Improuvement', 'Improvement'), ('Task', 'Task')], default='Bug', max_length=15)),
                ('priority', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('HIGH', 'High')], default='Low', max_length=10)),
                ('status', models.CharField(choices=[('To do', 'To Do'), ('Work in process', 'Wip'), ('Done', 'Done')], default='To do', max_length=50)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('assignee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignee', to=settings.AUTH_USER_MODEL)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_issue', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue_project', to='project.project')),
            ],
        ),
        migrations.AddField(
            model_name='contributor',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contributor_project', to='project.project'),
        ),
        migrations.AddField(
            model_name='contributor',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contributor_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=5000)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_comment', to=settings.AUTH_USER_MODEL)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue_comment', to='project.issue')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='contributor',
            unique_together={('user', 'project')},
        ),
    ]
