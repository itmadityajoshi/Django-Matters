
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

from django.urls import include
urlpatterns += [path('student/', include('student.urls'))]
