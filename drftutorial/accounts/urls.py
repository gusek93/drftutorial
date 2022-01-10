from django.urls import path, include
from .views import UserCreate
from rest_framework import urls


urlpatterns = [
    path('signup/', UserCreate.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
