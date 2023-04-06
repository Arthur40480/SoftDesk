from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from .models import Project, Contributor
from .serializers import ProjectSerializer
from .permissions import IsAuthorOrReadOnly


class ProjectCreateAndList(APIView):

    """
    Méthode POST permettant de créer un Projet
    """

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    Méthode GET qui récupère la liste de tous les projets rattachés à l'utilisateur connecté 
    Si auteur
    Si contributeur
    """

    def get(self, request):

        if request.user.is_authenticated:
            user = request.user
            projects = Project.objects.filter(author=user) | Project.objects.filter(contributor=user)

            if projects:
                serializer = ProjectSerializer(projects, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)

            else:
                return Response({"message": "Aucun projet relier à cet utilisateur."}, status=status.HTTP_404_NOT_FOUND)

        else:
            return Response({"message": "Vous n'êtes pas connecter. "})


class ProjectDetail(APIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_project(self, pk):
        try:
            project = Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404("Le projet recherché n'existe pas")
        return project

    def get(self, request, pk):
        project = Project.objects.get(pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        project = self.get_project(pk)
        serializer = ProjectSerializer(project, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk):
        try:
            project = Project.objects.get(pk=pk)
            project.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Project.DoesNotExist:
            raise Http404("Le projet recherché n'existe pas")