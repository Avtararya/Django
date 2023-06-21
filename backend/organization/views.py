from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Branch, Master
from .serializers import BranchSerializer, CompanyMasterSerializer


@api_view(["GET", "POST", "PUT", "DELETE"])
def createOrganization(request):
    if request.method == "GET":
        pass

    if request.method == "POST":
        pass

    if request.method == "PUT":
        pass

    if request.method == "DELETE":
        pass
