from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('HelloWorld.urls')),  # Include HelloWorld app URLs at the root level
    path('admin/', admin.site.urls),
]
