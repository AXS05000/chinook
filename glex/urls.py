from django.urls import path
from .views import HomeGlex, HomeGlex2

urlpatterns = [
    path("home_glex", HomeGlex.as_view(), name="home_glex"),
    path("home_glex2", HomeGlex2.as_view(), name="home_glex"),
]
