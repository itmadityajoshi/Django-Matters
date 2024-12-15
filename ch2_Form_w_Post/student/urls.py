from django.urls import path
from student.views import register
urlpatterns = [
    path('student/register/', register, name='register'),
]
