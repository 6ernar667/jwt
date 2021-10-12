from django.contrib import admin
from django.urls import path, include
from accounts.views import ListUsers, CustomAuthToken

urlpatterns = [
    path('api/users/', ListUsers.as_view()),
    path('api/token/auth/', CustomAuthToken.as_view()),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
