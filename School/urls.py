from rest_framework.authtoken import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/',include('classroom.api.urls')),
    path('api-auth/',include('rest_framework.urls')),
    path('api-auth/',include('rest_framework.urls')),
    path('api-token-auth/',views.obtain_auth_token)
]
