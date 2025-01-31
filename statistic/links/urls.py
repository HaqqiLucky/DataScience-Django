from django.urls import path
from . import views

app_name = "links"

urlpatterns = [
    path('', views.link_list, name="list"),
    path('<slug:slug>', views.link_page, name="page")
]

