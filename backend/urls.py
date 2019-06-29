from django.conf.urls import url,include
from backend import views
from django.urls import path

urlpatterns = [
    path('testapi/', views.testapi, name='testapi'),
]

