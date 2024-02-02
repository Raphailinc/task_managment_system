from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.authentication.urls')),
    path('', include('myapp.tasks.urls')),
]