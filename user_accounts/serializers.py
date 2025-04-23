from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator

from. import models


User = get_user_model()

#register serializer

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    #username validation
    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already taken.")
        return value
    
    #email validation
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("email already taken.")
        return value
    

    #password validation

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords must match."})
        try:
            validate_password(attrs['password'])  # uses Django's built-in validators
        except ValidationError as e:
            raise serializers.ValidationError({"password": e.messages})
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user

# serializer class for login authentication

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only = True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(email=email, password=password)

            if not user:
                raise serializers.ValidationError(_("Invalid login credentials"))
            if not user.is_active:
                raise serializers.ValidationError(_("User account is disabled"))
        else:
            raise serializers.ValidationError(_("must include both email and password"))
        attrs['user'] = user
        return attrs

# serializer class for password reset

class PasswrodResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("No user is associated with this email")
        return value

# serializer to confirm the new password

class PasswordResetCOnfirmSerializer(serializers.Serializer):
    uid = serializers.CharField()
    token = serializers.CharField()
    new_password = serializers.CharField(write_only = True)

    def validate_new_password(self, value):
        validate_password(value)
        return value
    
    def validate(self, attrs):
        try:
            uid = urlsafe_base64_decode(attrs['uid']).decode()
            user = user.objects.get(pk=uid)
        except (User.DoesNotExist, ValueError, TypeError):
            raise serializers.ValidationError("Invalid user.")
        
        if not default_token_generator.check_token(user, attrs['token']):
            raise serializers.ValidationError("Invalid or expired token.")
        
        attrs['user'] = user
        return attrs
    

    def save(self):
        user = self.validated_data['user']
        user.set_password(self.validated_data['new_password'])
        user.save()


# class of farmer serializer
class FarmerProfileEditSerializer(serializers.Serializer):
    class Meta:
        model = models.FarmerProfileEdit
        fields = '__all__'

class FarmerProfileModelSerializer(serializers.Serializer):
    class Meta:
        model = models.FarmerProfileModel
        fields = '__all__'

class ProductListSerializer(serializers.Serializer):
    class Meta:
        model = models.ProductList
        fields = '__all__'

