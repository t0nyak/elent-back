from django.urls import path, include
from rest_framework import routers, viewsets
from . import views
from .models import Fee, FeeDistribution, Project, Socio
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
# router.register(r'authors', AuthorViewSet)
# router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('projects/last', views.LastProjects.as_view())
    # path('projects/', views.PostList.as_view()),
    # path('posts/<str:pk>', views.PostDetail.as_view()),
    # path('authors/', views.authors),
    # path('categories/', views.categories)
]