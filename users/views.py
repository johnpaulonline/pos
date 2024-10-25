from django.contrib.auth.models import Group
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import CustomUser
from .serializers import CustomUserSerializer, CustomerRegistrationSerializer, CustomTokenObtainPairSerializer


class UserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        role = self.request.data.get('role')

        if role == 'Customer':
            group = Group.objects.get(name='Customer')
        elif role == 'Business':
            group = Group.objects.get(name='Business')
        elif role == 'BackOffice':
            group = Group.objects.get(name='BackOffice')
        else:
            group = None

        if group:
            user.groups.add(group)

        user.save()


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomerRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomerRegistrationSerializer
    permission_classes = [AllowAny]
