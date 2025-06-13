# user/views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer
from rest_framework import status, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .tasks import send_verification_email  # Import the Celery task for sending emails
# Create your views here.

# User registration view to handle user creation
class RegisterView(APIView):
    def post(self, request):
        serializer= RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user= serializer.save()
            send_verification_email.delay(user.email, user.username) # Call the Celery task to send verification email
            return Response({'message': 'User registered successfully and verification email sent!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



from .serializers import NewsSerializer
from .models import News
# View to handle news creation and listing
class NewsView(generics.ListCreateAPIView):
    queryset= News.objects.all()
    serializer_class= NewsSerializer
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return [AllowAny()]
    
    def get_serializer_context(self):
        return {'request': self.request}
    