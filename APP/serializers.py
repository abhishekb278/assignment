from rest_framework import serializers

from .models import *
from django.core.exceptions import ValidationError

from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class Signup_slr(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True,write_only=True,validators=[validate_password])
    email = serializers.EmailField(required=True,write_only=True)
    phone = serializers.IntegerField(required=True,write_only=True)
    avatar = serializers.FileField(required=True,write_only=True)

    class Meta:
        model=User
        fields=('username','name','phone','email','password','password2','avatar')

    def validate(self,values):
        if values['password']!=values['password2']:
            raise serializers.ValidationError('Password did not get matched')
        else:
            pass
        return values

    def create(self,values):
        del values['password2']
        user=User.objects.create(**values)
        user.set_password(values['password'])
        user.save()
        return user

from django.contrib.auth import authenticate
class Login_slr(serializers.ModelSerializer):
    username=serializers.CharField()
    password=serializers.CharField()
    class Meta:
        model=User
        fields=('username','password')
    
    def validate(self,values):
        user = authenticate(username=values['username'], password=values['password'])
        if user is not None:
            return user
        else:
            raise serializers.ValidationError("Invalid login credentials")
            return None

class User_slr(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name','phone','email','avatar']

