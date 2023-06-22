from django.urls import path

from . import views

urlpatterns = [
    path("/getAll", views.getAllOrganizations),
    path("/create", views.createOrganization),
    path("/create-branch", views.createBranch),
]
