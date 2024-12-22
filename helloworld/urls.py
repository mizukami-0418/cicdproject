from django.contrib import admin
from django.urls import path
from helloworldapp import views


from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),    
]
