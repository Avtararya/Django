from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework import status

@api_view(['GET'])
def get_customers(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def filter_customers(request):
    type_ = request.data.get('type')
    query = request.data.get('query')

    if type_ == "customer_id":
        customers = Customer.objects.filter(customer_id=query)
    elif type_ == "genre":
        customers = Customer.objects.filter(genre__iexact=query)
    elif type_ == "age":
        customers = Customer.objects.filter(age=query)
    elif type_ == "annual_income":
        customers = Customer.objects.filter(annual_income=query)
    elif type_ == "spending_score":
        customers = Customer.objects.filter(spending_score=query)
    else:
        return Response({"error": "Invalid type"}, status=400)

    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_customer(request):
    if request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
