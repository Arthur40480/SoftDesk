from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from .models import Project
from .serializers import ProjectSerializer
from .permissions import IsAuthorOrReadOnly



class ProjectCreateAndList(APIView):
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProjectUpdate(APIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    def get_project(self, pk):
        try:
            project = Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404("Le projet recherché n'existe pas")
        return project

    def patch(self, request, pk):
        project = self.get_project(pk)
        serializer = ProjectSerializer(project, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)


class ProjectDelete(APIView):

    def delete(self, request, pk):
        try:
            project = Project.objects.get(pk=pk)
            project.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Project.DoesNotExist:
            raise Http404("Le projet recherché n'existe pas")
