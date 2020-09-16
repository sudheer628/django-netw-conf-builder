from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
]
#here views.index means calling index function from views.py