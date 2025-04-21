from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from . import models
from . import serializers

from django.contrib.auth import get_user_model
from .utils import send_password_reset_email
from django.db import IntegrityError


User = get_user_model()


# APIView for the register serializer

class RegisterView(APIView):
    def post(self, request):
        print("📥 RegisterView hit")
        serializer = serializers.RegisterSerializer(data=request.data)

        if serializer.is_valid():
            try:
                # If the serializer is valid, save the user
                user = serializer.save()
                return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)

            except IntegrityError:
                return Response({"error": "Username or email already exists"}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                print(f"Unexpected error during registration: {e}")  # Add this
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# APIView for the login serializer

class LoginView(APIView):
    def post(self, request):
        serializer = serializers.LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password']
            )
            if user:
                token, create = Token.objects.get_or_create(user=user)
                return Response({"token": token.key})
            return Response({"error": "Invalid credentials"}, status=400)
        return Response(serializer.errors, status=400)


#APIView for password reset serializer

class PasswordResetRequestView(APIView):
    def post(self, request):
        serializer = serializers.PasswrodResetRequestSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = User.objects.get(email=email)
            send_password_reset_email(user)
            return Response({"message": "Password reset email sent"})
        return Response(serializer.errors, status=400)
    


# now we create modelviewsets for the other models that require CRUD APIs

#modelviewset for FarmerProfileEditSerializer

class FarmerProfileEditViewSet(ModelViewSet):
    queryset = models.FarmerProfileEdit.objects.all()
    serializer_class = serializers.FarmerProfileEditSerializer


#viewset for FarmerProfileModelSerializer

class FarmerProfileModelViewSet(ModelViewSet):
    queryset = models.FarmerProfileModel.objects.all()
    serializer_class = serializers.FarmerProfileModelSerializer

#viewset for productListSerializer

class ProductListViewSet(ModelViewSet):
    queryset = models.ProductList.objects.all()
    serializer_class = serializers.ProductListSerializer

# Create your views here.
