from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from .models import Project, Contributor, Issue, Comment


class ProjectPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        project = get_object_or_404(Project, id=view.kwargs['project_pk'])
        try:
            if request.method in permissions.SAFE_METHODS:
                return project.author or Contributor.objects.get(user=request.user, project=project)
            return request.user == project.author

        except KeyError:
            return True


class ContributorPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        project = get_object_or_404(Project, id=view.kwargs['project_pk'])
        try:

            if request.method in permissions.SAFE_METHODS:
                return project.author == request.user or Contributor.objects.get(user=request.user, project=project)
            return project.author == request.user

        except Contributor.DoesNotExist:
            return False


class IssuePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        project = get_object_or_404(Project, id=view.kwargs['project_pk'])
        try:

            if request.method in ['GET', 'POST']:
                return project.author == request.user or Contributor.objects.get(user=request.user, project=project)

            elif request.method in ['PUT', 'DELETE']:
                issue = get_object_or_404(Issue, id=view.kwargs['issue_pk'])
                return issue.author == request.user

        except Contributor.DoesNotExist:
            return False


class CommentPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        project = get_object_or_404(Project, id=view.kwargs['project_pk'])
        try:

            if request.method in ['GET', 'POST']:
                return project.author == request.user or Contributor.objects.filter(user=request.user, project=project).exists()

            elif request.method in ['PUT', 'DELETE']:
                comment = get_object_or_404(Comment, id=view.kwargs['comment_pk'])
                return comment.author == request.user

        except Contributor.DoesNotExist:
            return False




