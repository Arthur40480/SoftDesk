from django.contrib import admin
from django.urls import path, include
from authentication.views import UserCreate
from project.views import ProjectCreateAndList, ProjectDetail
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/users/', UserCreate.as_view(), name='signup'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/projects/', ProjectCreateAndList.as_view(), name='create_project'),
    path('api/projects/<int:project_pk>/', ProjectDetail.as_view(), name='create_project')
]