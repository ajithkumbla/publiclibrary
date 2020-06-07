from django.urls import path
from . import views


urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
	path('review/<str:pk>/', views.review, name="review"),
	path('submit_post/',views.submit_post,name="submit_post"),
    path('', views.home, name="home"),
]
