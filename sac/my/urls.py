from django.urls import path
from . import views

urlpatterns=[
    path("", views.base , name="base"),
    path("details/<int:product_id>",views.details,name="details"),
    path("add", views.add,name="add"),
    

]
