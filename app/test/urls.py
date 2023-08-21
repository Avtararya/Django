from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('generate-xml/', views.generate_invoice_xml, name='generate_invoice_xml'),
]
