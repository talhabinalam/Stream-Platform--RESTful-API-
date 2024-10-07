from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from . import models

class RegisterView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()

            data['response'] = "Registration Successful"
            data['username'] = account.username
            data['email'] = account.email

            # TokenAuthentication
            token = Token.objects.get(user=account).key
            data['token'] = token

            # JWTAuthentication
            # refresh = RefreshToken.for_user(account)
            # data['refresh'] = {
            #     'refresh': str(refresh),
            #     'access': str(refresh.access_token),
            # }

        else:
            data = serializer.errors

        return Response(data, status=status.HTTP_201_CREATED)



class LogotView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.is_authenticated:
            request.user.auth_token.delete()
            return Response({"message": "User logged out successfully!"}, status=status.HTTP_200_OK)
        return Response({"message": "User must login first!"}, status=status.HTTP_400_BAD_REQUEST)
