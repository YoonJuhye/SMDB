from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer, ProfileImg

User = get_user_model()

@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
def profileimg(request, username):
    user = get_object_or_404(User, username=username)
    serializer = ProfileImg(user)
    return Response(serializer.data)

@api_view(['POST'])
def saveImg(request, user_pk):
    user = get_object_or_404(Profile, user_id=user_pk)
    serializer = ProfileImg(instance=user, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
