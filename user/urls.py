# user/urls.py

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, NewsView

urlpatterns=[
# URL patterns for user authentication- token generation and refresh
    path('token/',TokenObtainPairView.as_view(), name= 'token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# URL patterns for user registration
    path('register/', RegisterView.as_view(), name='register'),
# URL patterns for news creation and listing
    path('news/', NewsView.as_view(), name='news_list_create'),
    path('news/<int:pk>/', NewsView.as_view(), name='news_detail'),
]


