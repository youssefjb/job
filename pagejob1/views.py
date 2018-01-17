from django.shortcuts import render
from rest_framework import generics
from pagejob1.permissions import IsAuthenticatedOrCreate
from pagejob1.serializers import SignUpSerializer
from django.contrib.auth.models import User

class SignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = (IsAuthenticatedOrCreate,)

