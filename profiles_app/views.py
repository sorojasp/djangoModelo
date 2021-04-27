from django.shortcuts import render
from rest_framework.views import APIView
from profiles_app import serializers
from rest_framework.response import Response
from rest_framework import status
from profiles_app import models


from example.hasher import hasher

# Create your views here.
class HelloView(APIView):
    """
    """

    serializers_class = serializers.HelloSerializer
    queryset_class = models.UserProfile.objects.all()
    hasher_obj=hasher.PBKDF2WrappedSHA1PasswordHasher()

    
 

    def post(self, request, format=None):
        """Create a hello message with our name"""

        password_encoded:str=self.hasher_obj.encode(request.data["password"],"recyapp",3)

        models.UserProfile.objects.create(email=request.data["email"],
                                          password=password_encoded

    
                                          
)

        print(f'clave es:{self.hasher_obj.verify(request.data["password"],password_encoded)}')

        return Response({'data': 'hello'}, status=status.HTTP_200_OK)
