from django.urls import path
from .views import signup,index,login


urlpatterns = [
   path("",index,name="index"),
   path("login",login,name="login"),
   

   path("signup",signup,name="signup")
]
