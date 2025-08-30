# serialisers that will convert python objects to json

from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

class RegistrationSerializer(serializers.ModelSerializer):
   email = serializers.EmailField(
       required = True,
       validators=[UniqueValidator(queryset=CustomUser.objects.all())]
   )
   password = serializers.CharField(
       required = True,
       write_only = True,
       validators=[validate_password]
   )
   password2 = serializers.CharField(write_only=True, required=True)
   
   class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'password2', 'bio', 'profile_picture')
        extra_kwargs = {
            'bio':{'required':False},
            'profile_picture':{'required': False},
        }
    
   def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match!"})
        return attrs
    
   def create(self, validated_data):
        validated_data.pop('password2')
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email = validated_data['email'],
            password=validated_data['password'],
            bio = validated_data['bio'],
            profile_picture= validated_data.get('profile_picture')
        )
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True,write_only=True)
    
    def validate(self, attrs):
        user = authenticate(username=attrs['username'], password=attrs['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials.')
        attrs['user'] = user
        return attrs

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    
    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs
    
    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail("bad_token")