from django.urls import path
from . import views
urlpatterns = [
    path('searvices/',views.searvices),
    path('shop/',views.searvices),

]