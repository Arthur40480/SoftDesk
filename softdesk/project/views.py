from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from .models import Project, Contributor, User, Issue
from .serializers import ProjectSerializer, ContributorSerializer, IssueSerializer
from .permissions import ProjectPermission, ContributorPermission, IssuePermission
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import NotFound

"""
PROJECT ENDPOINT
"""
class ProjectCreateAndList(APIView):

    permission_classes = [permissions.IsAuthenticated]

    """
    Méthode création de projet ➡ POST
    Permission ➡ N'importe quel utilisateur connecter
    """

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    Méthode affichage de tous les projets rattachés à l'utilisateur connecté ➡ GET
    Permission ➡ Auteur ou contributeur
    """

    def get(self, request):
        user = request.user
        projects = Project.objects.filter(author=user) | Project.objects.filter(contributor=user)

        if projects:
            serializer = ProjectSerializer(projects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response({"message": "Aucun projet relier à cet utilisateur."}, status=status.HTTP_404_NOT_FOUND)


class ProjectDetail(APIView):

    permission_classes = [permissions.IsAuthenticated, ProjectPermission]

    def get_project(self, project_pk):
        try:
            return Project.objects.get(id=project_pk)
        except Project.DoesNotExist:
            raise Http404()

    """
    Méthode affichage de tous les détails d'un projet ➡ GET
    Permission ➡ N'importe quel utilisateur connecter
    """
    def get(self, request, project_pk):
        project = self.get_project(project_pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)

    """
    Méthode de mise à jour d'un projet ➡ PUT
    Permission ➡ Auteur uniquement
    """
    def put(self, request, project_pk):
        project = self.get_project(project_pk)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)

    """
    Méthode de suppression d'un projet ➡ DELETE
    Permission ➡ Auteur uniquement
    """
    def delete(self, request, project_pk):
        project = self.get_project(project_pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ContributorCreateandList(APIView):

    permission_classes = [permissions.IsAuthenticated, ContributorPermission]

    """
    Méthode affichage de tous les contributeurs rattachés à un projet ➡ GET
    Permission ➡ N'importe quel utilisateur connecter
    """
    def get(self, request, project_pk):
        project = get_object_or_404(Project, id=project_pk)
        contributor = Contributor.objects.filter(project=project)
        serializer = ContributorSerializer(contributor, many=True)
        return Response(serializer.data)

    """
    Méthode d'ajout d'un contributeur à un projet ➡ POST
    Permission ➡ Auteur uniquement
    """
    def post(self, request, project_pk):
        project = get_object_or_404(Project, id=project_pk)
        data = request.data.copy()
        data['project'] = project.id
        try:
            print(request.data)
            Contributor.objects.get(user=data['user'], project=project.id)
            return Response({"message": "Ce contributeur existe déjà !"}, status=status.HTTP_400_BAD_REQUEST)
        except Contributor.DoesNotExist:
            try:
                User.objects.get(id=data['user'])
                serializer = ContributorSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except User.DoesNotExist:
                return Response({"message": "Cet utilisateur est introuvable !"}, status=status.HTTP_404_NOT_FOUND)


class ContributorDetail(APIView):

    permission_classes = [permissions.IsAuthenticated, ContributorPermission]

    """
    Méthode de suppression d'un contributeur à un projet ➡ DELETE
    Permission ➡ Auteur uniquement
    """
    def delete(self, request, project_pk, contributor_pk):
        contributor = get_object_or_404(Contributor, id=contributor_pk)
        contributor.delete()
        return Response({"message": "Le contributeur à bien été supprimer"}, status=status.HTTP_204_NO_CONTENT)


class IssueCreateAndList(APIView):

    permission_classes = [permissions.IsAuthenticated, IssuePermission]

    """
    Méthode d'affichage des problèmes d'un projet ➡ GET
    Permission ➡ Auteur ou contributeur
    """
    def get(self, request, project_pk):
        project = get_object_or_404(Project, id=project_pk)
        issue = Issue.objects.filter(project=project)
        serializer = IssueSerializer(issue, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    """
    Méthode de création d'un problème dans un projet ➡ POST
    Permission ➡ Auteur ou contributeur
    """
    def post(self, request, project_pk):
        serializer = IssueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IssueDetail(APIView):

    permission_classes = [permissions.IsAuthenticated, IssuePermission]

    """
    Méthode d'actualisation d'un problème dans un projet ➡ PUT
    Permission ➡ Auteur uniquement
    """
    def put(self, request, project_pk, issue_pk):
        issue = get_object_or_404(Issue, id=issue_pk)
        serializer = IssueSerializer(issue, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)

    """
    Méthode de suppression d'un problème dans un projet ➡ DELETE
    Permission ➡ Auteur uniquement
    """
    def delete(self, request, project_pk, issue_pk):
        issue = get_object_or_404(Issue, id=issue_pk)
        issue.delete()
        return Response({"message": "Problème supprimer !"}, status=status.HTTP_204_NO_CONTENT)