from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .models import RoomDetails, MyBooking, Contact, Gallery
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class HomePage(View):
    def get(self, request):
        rooms = RoomDetails.objects.all()
        context = {'rooms': rooms}
        return render(request, 'index.html', context=context)


class AboutPage(View):
    def get(self, request):
        return render(request, 'about.html')


@method_decorator(login_required(login_url='/login'), name='dispatch')
class BookingView(View):
    def get(self, request):
        return render(request, 'bookings.html')


class ContactView(View):

    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            contact = Contact(name=name, email=email, message=message, subject=subject)
            contact.save()
            messages.success(request, 'Your Inquiry has been submitted. Thank you!')
            return redirect("contact")
        messages.error(request, 'There is problem with submission. Please Try Again')
        return redirect("contact")


class RegisterView(View):
    def get(self, request):
        return render(request, 'create.html')

    def post(self, request):
        if request.method == "POST":
            email = request.POST.get('email')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            password = request.POST.get('password')
            password_cf = request.POST.get('confirm_pw')

            if password == password_cf:
                if User.objects.filter(username=email).exists():
                    message = "User already exists."
                    print(message)
                else:
                    user = User.objects.create_user(username=email,
                                                    first_name=first_name,
                                                    last_name=last_name,
                                                    password=password)
                    user.save()
                    return redirect("login")
            else:
                message = "Passwords do not match"
                print(message)
            context = {
                'error_msg': message
            }
            return render(request, 'create.html', context=context)
        else:
            return render(request, 'create.html')


class ForgetPasswordView(View):
    def get(self, request):
        return render(request, 'forgetPassword.html')


class GalleryView(View):
    def get(self, request):
        images = Gallery.objects.all()
        context = {'images': images}
        return render(request, 'Gallery.html', context=context)


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        if request.method == "POST":
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = auth.authenticate(username=email, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("home")
            else:
                message = "Invalid login details."
                print(message)
                return redirect("login")
        else:
            return render(request, 'login.html')


@method_decorator(login_required(login_url='/login'), name='dispatch')
class MyBookingsView(View):
    def get(self, request):
        try:
            my_bookings = MyBooking.objects.get(name=request.user)
        except:
            my_bookings = ""
        context = {'my_booking': my_bookings}
        return render(request, 'myBookings.html', context=context)

    def post(self, request):
        if request.method == 'POST':
            arrival_date = request.POST.get('arrival_date')
            departure_date = request.POST.get('departure_date')
            room = request.POST.get('room')
            nights = request.POST.get('nights')
            adults = request.POST.get('adults')
            children = request.POST.get('children')
            number = request.POST.get('number')
            message = request.POST.get('message')
            has_made_booking = MyBooking.objects.all().filter(name=request.user)
            if has_made_booking:
                messages.error(request, 'Your have already made booking.')
                return redirect('booking')
            book = MyBooking(name=request.user, arrival_date=arrival_date, departure_date=departure_date,
                             room_select=room,
                             num_nights=nights, num_person=adults, num_children=children, phone_num=number, des=message)
            book.save()
            return redirect('my_bookings')
        return redirect('booking')


class LogoutView(View):
    def get(self, request):
        auth.logout(request)
        return redirect("login")
