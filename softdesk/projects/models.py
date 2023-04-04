from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):

    class Type(models.TextChoices):
        BACK_END = "Back-end"
        FRONT_END = "Front-end"
        IOS = 'IOS'
        ANDROID = 'Android'

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=5000, blank=True)
    type = models.fields.CharField(choices=Type.choices, max_length=15, default="Back-end")
    users = models.ManyToManyField(User, through='Contributors', related_name='contributor')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_author')


class Contributors(models.Model):

    class Permission(models.TextChoices):
        ADMIN = "Admin"
        LIST = "list"
        DELETE = "Delete"
        UPDATE = "Update"

    user = models.ForeignKey(User, on_delete=models.CASCADE, default="1")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default="1")
    permission = models.fields.CharField(choices=Permission.choices, max_length=15, default="Admin")
    role = models.fields.CharField(max_length=50)


class Issue(models.Model):

    class Priority(models.TextChoices):
        LOW = 'Low'
        MEDIUM = 'Medium'
        HIGH = 'HIGH'

    class Tag(models.TextChoices):
        BUG = 'Bug'
        IMPROVEMENT = 'Improuvement'
        TASK = 'Task'

    class Status(models.TextChoices):
        TO_DO = 'To do'
        WIP = 'Work in process'
        Done = 'Done'

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=5000, blank=True)
    priority = models.fields.CharField(choices=Priority.choices, max_length=10, default="Low")
    tag = models.fields.CharField(choices=Tag.choices, max_length=15, default="Bug")
    status = models.fields.CharField(choices=Status.choices, max_length=50, default="To do")
    creation_date = models.fields.DateTimeField(auto_now_add=True)
    # ForeignKey assignee user_id
    # ForeignKey author user_id
    # ForeignKey project_id


class Comment(models.Model):

    description = models.fields.CharField(max_length=5000)
    creation_date = models.fields.DateTimeField(auto_now_add=True)
    # ForeignKey issue_id
    # ForeignKey author user_id