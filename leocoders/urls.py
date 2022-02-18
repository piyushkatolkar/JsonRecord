from django.contrib import admin
from django.urls import path
from restapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/', views.student_detail),
    path('stuinstance/<int:pk>', views.student_instance),
    path('stulist/', views.student_list),
]
