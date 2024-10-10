from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name="home"),
    path('page-2', views.page2, name="page2"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('signout',views.signout,name="signout"),
]


