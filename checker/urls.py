from django.urls import path
from . import views

urlpatterns = [path("", views.ping_form_view, name="ping-checker")]
