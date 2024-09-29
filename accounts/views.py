from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class RegisterView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
