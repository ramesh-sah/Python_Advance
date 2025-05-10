from mysite import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Course,name='course'),
    path('about/',views.About, name='about'),
    path('course/<int:courseid>/',views.courseDetails),
    path('coursedeatils/<str:courseName>/',views.courseDetailsInString),
]
