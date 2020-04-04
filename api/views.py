from django.shortcuts import render
from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer


# Create your views here.
class LastProjects(generics.ListAPIView):
    queryset = Project.objects.filter(visible=True).order_by('-created_on')[:3]
    serializer_class = ProjectSerializer
