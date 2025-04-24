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

from rest_framework.utils.serializer_helpers import ReturnDict


User = get_user_model()


# APIView for the register serializer

class RegisterView(APIView):
    def post(self, request):
        print("📥 RegisterView hit")
        serializer = serializers.RegisterSerializer(data=request.data)

        print("🧪 Serializer created")

        if serializer.is_valid():

            print("✅ Serializer is valid")

            try:
                # If the serializer is valid, save the user
                user = serializer.save()

                print("🙌 User saved")

                return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)

            except IntegrityError:

                print("⚠️ Integrity error")

                return Response({"error": "Username or email already exists"}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                print(f"Unexpected error during registration: {e}")  # Add this
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        errors = serializer.errors
        if isinstance(errors, ReturnDict):
            errors = dict(errors)  # Ensure JSON-safe
            
        print("❌ Serializer is invalid:", serializer.errors)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# APIView for the login serializer

class LoginView(APIView):
    def post(self, request):

        print("📩 Login request received")

        serializer = serializers.LoginSerializer(data=request.data)

        try:
            print("🧪 Calling is_valid()")
            if serializer.is_valid():
                print("✅ Serializer is valid")

                user = serializer.validated_data['user']
                print("🔐 Authenticated user:", user)

                print("🧪 Token class being used:", Token)

                token, created = Token.objects.get_or_create(user=user)
                print(f"🔑 Token: {token.key} | Created: {created}")

                return Response({"token": token.key,
                                 "user": {
                                     "role": user.role
                                 }
                                 }, 
                                
                                status=status.HTTP_200_OK)

            print("❌ Invalid data:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(f"🔥 Exception during login: {e}")
            return Response(
                {"error": "Internal server error", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


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
