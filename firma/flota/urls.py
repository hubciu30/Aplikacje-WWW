from django.urls import path
from . import views


urlpatterns = [
    path('osoby', views.OsobaList.as_view()),
    path('osoby/<int:pk>', views.OsobaList.as_view()),
]
