from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken import views


endpoints = [
    path('auth/', views.obtain_auth_token),
    path('core/', include('core.urls')),
    path('dosimetria/', include('dosimetria.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(endpoints)),
]
