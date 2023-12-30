from api import views
from rest_framework import routers
from django.urls import path, include
router = routers.DefaultRouter()
router.register(r'singer', views.SingerViewSet)
router.register(r'song', views.SongViewSet)

urlpatterns = [
    path('', include(router.urls))

]
