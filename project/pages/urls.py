from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('login', views.LoginView.as_view(), name='login'),
    path('booking', views.BookingView.as_view(), name='booking'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('about', views.AboutPage.as_view(), name='about'),
    path('forget-pw', views.ForgetPasswordView.as_view(), name='forget_pw'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('gallery', views.GalleryView.as_view(), name='gallery'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('my-bookings', (views.MyBookingsView.as_view()), name='my_bookings'),
]
