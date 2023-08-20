from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from django.contrib.auth import authenticate
import jwt
import datetime
from django.conf import settings


# Create your views here.
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            serializer = UserSerializer(user)
            payload = {
                "user_id": user.id,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
            }
            token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
            data = serializer.data
            data["tokens"] = {"access_token": str(token)}
            response_data = {
                "user": data,
            }
            response = Response(response_data, status=status.HTTP_200_OK)
            return response
        return Response(
            {"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


class LogoutView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        response = Response({"msg": "User logged out!"}, status=status.HTTP_200_OK)
        return response
