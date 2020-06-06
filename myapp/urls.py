from django.urls import path
from . import views


urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
	path('review/<str:pk>/', views.review, name="review"),
	path('submitrev/',views.submitrev, name="submitrev"),
    path('', views.home, name="home"),

]
