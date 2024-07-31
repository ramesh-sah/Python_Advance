from django.contrib import admin
from django.urls import path, include  # Import include here
from todos import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todos.urls')),  # Include the 'todos' app URLs here
]
