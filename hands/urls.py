from django.urls import path,include
from hands import views

urlpatterns = [
    path('',views.index)
]
