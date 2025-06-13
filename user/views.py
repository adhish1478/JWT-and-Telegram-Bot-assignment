# user/views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer
from rest_framework import status, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
# Create your views here.

# User registration view to handle user creation
class RegisterView(APIView):
    def post(self, request):
        serializer= RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user= serializer.save()
            return Response({'message': 'User registered successfully!'}, status=status.HTTP_201_CREATED)
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
    