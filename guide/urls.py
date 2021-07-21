from django.urls import path, include
from .views import guidehome
urlpatterns = [
    path('', guidehome, name='home'),

]
