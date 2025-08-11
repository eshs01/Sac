from django.urls import path
from . import views

urlpatters=[
    path("", views.base , name="base"),
    path("details/",views.details,name="details")

]
