from django.shortcuts import render

# from django.shortcuts import render

from rest_framework_jwt.serializers import jwt_payload_handler
import jwt
from django.contrib.auth.hashers import Argon2PasswordHasher

from rest_framework.decorators import api_view, schema

import numpy as np

# read env
import environ

env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env('.env')

# Create your views here.

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.decorators import permission_classes

# MAILER
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.tokens import PasswordResetTokenGenerator


@api_view(['POST'])
@permission_classes([AllowAny, ])
def login(request):
    email = request.data['email']
    password = request.data['password']

    return Response({'error': 0}, status.HTTP_200_OK)



