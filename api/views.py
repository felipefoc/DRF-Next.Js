from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .serializers import RegisterSerializer, ListUsersSerializers 
from rest_framework import status


class HelloView(APIView):
    permission_classes = (IsAuthenticated ,)
    def get(self, request):
        content = {'message': 'Got it'}
        return Response(content)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
        
class ListView(APIView):
    def get(self, request):
        permission_class = (IsAdminUser, )
        queryset = User.objects.all()
        serializer = ListUsersSerializers(queryset, many=True)
        return Response(serializer.data)


