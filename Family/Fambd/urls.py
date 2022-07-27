from django.urls import path
from Fambd.views import Family, addFamily

urlpatterns = [
    path("family/", Family, name="family"),
    path("add-family/", addFamily, name="add-family")
]
