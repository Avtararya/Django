from django.urls import path
from .views import generate_invoice_xml

urlpatterns = [
    path('generate_invoice_xml/', generate_invoice_xml, name='generate_invoice_xml'),
]
