from django.db import connection
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer, UserSerializer2
from django.contrib.auth import authenticate
import logging
from django.contrib.auth.hashers import check_password       
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission
from superuser.models import SuperUser


class UserRegisterAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            if User.objects.filter(email=email).exists():
                return Response({"message": "User with this email already exists"}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IsSuperUser(BasePermission):
    """
    Custom permission class to check if the user is a superuser.
    """

    def has_permission(self, request, view):
        return isinstance(request.user, SuperUser)

class UserStatusAPIView(APIView):
    permission_classes = [IsSuperUser]

    def get(self, request):
        user = request.user 
        is_admin = user.is_admin  
        return Response({'is_admin': is_admin})
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import jwt



class UserLoginAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        if user is None:
            print("user is none wtf")
        if not check_password(password, user.password):
            print("password is wrong")
        if user is not None and check_password(password, user.password):
            print("User data:", user.__dict__)
            # Token payload
            payload = {
            'id': user.pk,    
            'email': user.email,
            'username': user.username,
            'age': user.age,
            'field_of_interest': user.field_of_interest,
            'phone': user.phone,
            'governorate': user.governorate,
            'is_verified': user.is_verified,
            'is_admin': user.is_admin,
            'cart': user.cart, 
            'ticket': user.tickets,
            }


            # Generate JWT token
            token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
            return Response({'token': token}, status=status.HTTP_200_OK)
            # return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        else:
            print("Authentication failed for email:", email)
            print("Authentication failed for password:", password)
            return Response({"message": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)




class UserListCreateAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            if User.objects.filter(email=email).exists():
                return Response({"message": "User with this email already exists"}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRetrieveUpdateDestroyAPIView(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer2(instance= user, data=request.data, partial=True)
            if serializer.is_valid():
                validated_data = serializer.validated_data
                print(validated_data)
                print("***********************************\n")  # Inspect validated data before saving
                serializer.save()
                print("***********************************\n")  # Inspect validated data before saving
                print(serializer.data)  # Print executed queries for debugging
                print("***********************************\n")  # Inspect validated data before saving

                return Response({"message": "User updated successfully"})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "User updated successfully"})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)

            # Deserialize request data using CartItemDeletionSerializer
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                item_id = serializer.validated_data['item_id']

                if item_id in user.cart:
                    user.cart.remove(item_id)
                    user.save()
                    return Response({"message": "Item removed from cart"}, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "Item not found in cart"}, status=status.HTTP_404_NOT_FOUND)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except User.DoesNotExist:
            return Response({"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
