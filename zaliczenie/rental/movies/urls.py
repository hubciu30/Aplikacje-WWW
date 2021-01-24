from django.urls import path
from . import views


urlpatterns = [
    path('clients', views.ClientList.as_view(), name=views.ClientList.name),
    path('clients/<int:pk>', views.ClientDetail.as_view(), name=views.ClientDetail.name),
    path('videos', views.VideoList.as_view(), name=views.VideoList.name),
    path('videos/<int:pk>', views.VideoDetail.as_view(), name=views.VideoDetail.name),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name)
]
