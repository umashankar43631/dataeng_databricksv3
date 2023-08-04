from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.allRelatedLinks, name="all_links" ),
]