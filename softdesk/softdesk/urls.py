from django.contrib import admin
from django.urls import path, include
from authentication.views import UserCreate
from project.views import ProjectCreateAndList, ProjectDetail, ContributorCreateandList, ContributorDetail, IssueCreateAndList, IssueDetail
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/users/', UserCreate.as_view(), name='signup'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/projects/', ProjectCreateAndList.as_view(), name='create_list_project'),
    path('api/projects/<int:project_pk>/', ProjectDetail.as_view(), name='detail_project'),
    path('api/projects/<int:project_pk>/user/', ContributorCreateandList.as_view(), name='create_list_contributor'),
    path('api/projects/<int:project_pk>/user/<int:contributor_pk>/', ContributorDetail.as_view(), name='detail_contributor'),
    path('api/projects/<int:project_pk>/issue/', IssueCreateAndList.as_view(), name='create_list_issue'),
    path('api/projects/<int:project_pk>/issue/<int:issue_pk>/', IssueDetail.as_view(), name='detail_issue')
]