# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("customers/", views.get_customers, name="get_data"),
    path("filter/", views.filter_customers, name="filter_data"),
    path("add/", views.add_customer, name="add_customer"),
]
