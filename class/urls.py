from django.urls import path
from . import views



urlpatterns = [
    path('', views.homepage,  name='homepage'),
    path('login/', views.login,  name='login'),
    path('classroom/lesson-studies/examples/practices/test', views.classroom,  name='classroom'),
    path('guestroom/', views.guestroom,  name='guestroom'),
    path('register/', views.register,  name='register'),
    


    path('improve-xl-at-ofiice', views.xltutorial,  name='xltutorial'),
    
]