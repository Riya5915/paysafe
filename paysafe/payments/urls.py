from django.urls import path
from . import views

app_name = "payments"
urlpatterns = [
    path("", views.index, name="index"),
    path("data/", views.getFormData, name="fetchdata"),
    path("checkout/", views.checkout, name="checkout"),
]