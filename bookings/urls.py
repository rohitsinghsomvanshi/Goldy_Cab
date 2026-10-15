
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("services/", views.services, name="services"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),

    # Taxi Route Detail Page
    path(
        "routes/<slug:slug>/",
        views.route_detail,
        name="route_detail"
    ),
]
