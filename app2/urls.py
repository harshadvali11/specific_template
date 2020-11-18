from django.urls import path

from app2 import views

app_name='app2'

urlpatterns=[
    path('second/',views.second,name='second'),
]