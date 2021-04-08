from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import TokenError, RefreshToken, Token, BlacklistMixin
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken


class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=64, min_length=6, write_only=True)
    confirm_password=serializers.CharField(max_length=64, min_length=6, write_only=True)

    class Meta:
        model=User
        fields=['username', 'email', 'password','confirm_password', 'is_staff']
       

    def create(self, validate_data):
        username=validate_data["username"]
        email=validate_data["email"]
        password=validate_data["password"]
        confirm_password=validate_data["confirm_password"]
        is_staff=validate_data["is_staff"]

        if User.objects.filter(username=username):
            raise serializers.ValidationError({"username":"usename already exists", "status_code":400})
        if User.objects.filter(email=email):
            raise serializers.ValidationError({"email": "email already exists", "status_code":400})
        if password !=confirm_password:
            raise serializers.ValidationError({"password": "password do not match", "status_code":400})

        user = User(username=username, email=email, is_staff=is_staff)
        user.set_password(password)
        user.save()
        return user

class BlacklistMixin(BlacklistMixin):
    def check_blacklist(self):
        jti = self.payload[api_settings.JTI_CLAIM]
        if BlacklistedToken.objects.filter(token__jti=jti).exists():
            return True
        return False

# save access token in Outstanding
class AccessToken(BlacklistMixin, Token):
    token_type = 'access'
    lifetime = api_settings.ACCESS_TOKEN_LIFETIME
    no_copy_claims = (
        api_settings.TOKEN_TYPE_CLAIM,
        'exp',
        api_settings.JTI_CLAIM,
        'jti',
    ) 


class LoginSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=255)
    password=serializers.CharField(max_length=64, min_length=6, write_only=True)

    class Meta:
        model=User
        fields=['username', 'password',]

    def validate(self, validate_data):
        username=validate_data.get("username", None)
        password=validate_data.get("password", None)

        # if not User.objects.filter(username=username):
        #     raise serializers.ValidationError({"username":"username does not exist"})

        try:
            user=authenticate(username=User.objects.get(email=username), password=password)
        except:
            user=authenticate(username=username, password=password) 

        if user is None:
            raise serializers.ValidationError({"login":"account incorrect", "status_code":400})
        validate_data['user']=user
        return validate_data

class ChangePasswordSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=255)
    password=serializers.CharField(max_length=64, min_length=6, write_only=True)
    confirm_password=serializers.CharField(max_length=64, min_length=6,write_only=True)
    password_old=serializers.CharField(max_length=64, min_length=6,write_only=True)
    
    class Meta:
        model=User
        fields=['username', 'password','confirm_password','password_old']

    def validate(self, validate_data): 
        username=validate_data.get('username', None)
        password=validate_data.get('password', None)
        confirm_password=validate_data.get('confirm_password', None)
        password_old=validate_data.get('password_old', None)        
        if password_old == password:
            raise serializers.ValidationError({"data":{"message": "the new password is the same as the old one", "status_code":400}})
        user=authenticate(username=username, password=password_old)
        if not user:
            raise serializers.ValidationError({"message": "old password is not correct",  "status_code":400})    
        if password !=confirm_password:
            raise serializers.ValidationError({"message": "password do not match",  "status_code":400})
        return validate_data

class ChangeProfileSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=255)
    email=serializers.CharField(max_length=255)

    class Meta:
        model=User
        fields=['username', 'email', 'last_name', 'first_name', 'address', 'avatar']

    def update(self, instance, validate_data):
        username=validate_data.get('username', None)
        email=validate_data.get('email', None)
        user= User.objects.get(email=email)
        if user and str(user.username)!=username:
            raise serializers.ValidationError({"email": "email already exists", "status_code":400})

        instance.last_name = validate_data.get('last_name', instance.last_name)
        instance.first_name = validate_data.get('first_name', instance.first_name)
        instance.email = validate_data.get('email', instance.email)
        instance.address = validate_data.get('address', instance.address)
        instance.avatar = validate_data.get('avatar', instance.avatar)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username', 'email', 'is_staff', 'is_active']

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username', 'email', 'is_staff', 'is_active']

    def update(self, instance, validate_data):
        instance.is_staff = validate_data.get('is_staff', instance.is_staff)
        instance.is_active = validate_data.get('is_active', instance.is_active)
        instance.save()
        return instance
        