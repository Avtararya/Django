from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Branch, Master
from .serializers import BranchSerializer, MasterSerializer


@api_view(["GET"])
def getAllOrganizations(request):
    return Response(request.data, status=400)

    
@api_view(["POST"])
def createOrganization(request):
    serializer = MasterSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=401)


    
@api_view(["POST"])
def createBranch(request):
    serializer = BranchSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=401)