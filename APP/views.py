from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.authtoken.models import Token

from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import *

from rest_framework.authentication import *
from rest_framework.permissions import *
from rest_framework.decorators import authentication_classes,permission_classes

# Create your views here.
@api_view(['POST'])
def sign(request):
    serializer=Signup_slr(data=request.data)
    data={'Sign_Up':'Something Went Wrong'}
    if serializer.is_valid():
        user=serializer.save()
        token = Token.objects.create(user=user)
        data['Sign_Up'] = 'registration done successfully'
        return Response(data)
    else:
        data=serializer.errors
        return Response(data)


from django.contrib.auth import login
@api_view(['POST'])
def login_(request):
    serializer=Login_slr(data=request.data)
    data={'login':'Done'}
    serializer.is_valid()
    if serializer.validated_data is not None and serializer.is_valid():
        user=serializer.validated_data
        login(request, user)
        token,created = Token.objects.get_or_create(user=user)
        data['token'] = str(token)
        data['user_id'] = user.user_id
        return Response(data)
    else:
        data=serializer.errors
        return Response(data)

from django.contrib.auth import get_user_model
User = get_user_model()

class show_data(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request,upk,format=None):
        queryset=User.objects.filter(user_id=upk)
        serializer=User_slr(queryset,many=True)
        return Response(serializer.data)

