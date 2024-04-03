from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CustomUserModelSerializer


class SignupView(View):
    def get(self, request):
        template = 'user_management/signup.html'
        context = {}
        return render(request, template, context)


class LoginView(View):
    def get(self, request):
        template = 'user_management/login.html'
        context = {}
        return render(request, template, context)


class SignupAPIView(APIView):
    def post(self, request):
        print(request.data)
        serializer = CustomUserModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        print(email)
        print(password)

        if not email or not password:
            return Response({'error': 'Email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Authenticate user
        user = authenticate(email=email, password=password)
        if not user:
            return Response({'error': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)

        # Delete old token
        Token.objects.filter(user=user).delete()

        # Create new token
        token = Token.objects.create(user=user)
        print(f"token--------------{token}")
        # request.session['token'] = token.key
        return Response({'token': token.key}, status=status.HTTP_200_OK)


class UserProfileAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        print(user)
        user = {
            'id': user.id,
            'email': user.email,
            'name': user.name,
        }
        print(user)

        return Response({'user': user})
