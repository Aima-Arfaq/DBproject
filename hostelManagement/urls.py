from django.contrib import admin
from django.urls import path
from hostelManagement import views

admin.site.site_header = "Hostel Admin"
admin.site.site_title = "Hostel Admin Portal"
admin.site.index_title = "Welcome to Hostel Admin Portal"

urlpatterns = [
    path("", views.index, name='hostelManagement'),
    path('signup/', views.signup, name='signup'), 
    path('signin/', views.signin, name='signin'),  
    path('home/', views.home, name='home'),  
    path('logout/', views.logout, name='logout'),

    #to just display data on frontend
    path('view_students/', views.view_students, name='view_students'),
    path('view_staff/', views.view_staff, name='view_staff'),
]
