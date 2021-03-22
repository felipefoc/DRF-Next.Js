from django.urls import path
from api import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('createuser/', views.RegisterView.as_view(), name='createuser'),
    path('users/', views.ListView.as_view(), name='listview'),
]