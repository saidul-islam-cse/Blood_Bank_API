from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .import serializers
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.


class RegisterView(APIView):
    def post(self, request):
        serializer = serializers.RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message":"Register Success!"})
    
class LoginView(TokenObtainPairView):
    serializer_class = serializers.LoginSerializers