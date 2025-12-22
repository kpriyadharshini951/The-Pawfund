from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('dogs',views.dogs,name="dogs"),
    path('donate/', views.donate, name='donate'),
    path('adopt/', views.adopt, name='adopt')
]