from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from .models import Project, Contributor
from .serializers import ProjectSerializer
from .permissions import ProjectPermission
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
