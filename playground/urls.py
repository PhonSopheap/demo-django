from django.urls import path
from .import views

# URLConf
urlpatterns = [
    path('student/', views.Student.as_view()),
]