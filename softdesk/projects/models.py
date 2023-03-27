from django.db import models


class Contributors(models.Model):

    # permission = models.fields.ChoiceFields
    role = models.fields.CharField(max_length=100)


class Projects(models.Model):

    class Type(models.TextChoices):
        BACK_END = "Back-end"
        FRONT_END = "Front-end"
        IOS = 'IOS'
        ANDROID = 'Android'

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=5000)
    type = models.fields.CharField(choices=Type.choices, max_length=15)
    # ForeignKey for author_user_id


class Issues(models.Model):

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
    description = models.fields.CharField(max_length=5000)
    priority = models.fields.CharField(choices=Priority.choices, max_length=10)
    tag = models.fields.CharField(choices=Tag.choices, max_length=15)
    status = models.fields.CharField(choices=Status.choices, max_length=50)
    creation_date = models.fields.DateTimeField(auto_now_add=True)
    # ForeignKey assignee user_id
    # ForeignKey author user_id
    # ForeignKey project_id


class Comments(models.Model):

    description = models.fields.CharField(max_length=5000)
    creation_date = models.fields.DateTimeField(auto_now_add=True)
    # ForeignKey issue_id
    # ForeignKey author user_id