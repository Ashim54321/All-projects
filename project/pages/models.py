from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class RoomDetails(models.Model):
    TYPE_CHOICES = (('Available', 'available'),
                    ('Unavailable', 'unavailable'))
    room_number = models.CharField(max_length=100)
    room_status = models.CharField(max_length=255, choices=TYPE_CHOICES, default='Unavailable')
    room_des = models.TextField(blank=True)
    price = models.IntegerField()
    image1 = models.ImageField(upload_to='rooms', blank=True)
    image2 = models.ImageField(upload_to='rooms', blank=True)
    image3 = models.ImageField(upload_to='rooms', blank=True)
    image4 = models.ImageField(upload_to='rooms', blank=True)

    def __str__(self):
        return self.room_number


class MyBooking(models.Model):
    room = models.ForeignKey(RoomDetails, on_delete=models.CASCADE, null=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    arrival_date = models.DateField(auto_now=True, null=True)
    departure_date = models.DateField(auto_now=True, null=True)
    ROOM_CHOICES = (('1', '1'),
                    ('2', '2'),
                    ('3', '3'),
                    ('4', '4'),
                    ('5', '5'),
                    ('6', '6'),)

    room_select = models.CharField(max_length=255, choices=ROOM_CHOICES, default='0', null=True)
    # num_rooms = models.IntegerField(null=True)
    num_nights = models.IntegerField(null=True)
    num_person = models.IntegerField(null=True)
    num_children = models.IntegerField(null=True, default=0)
    phone_num = models.IntegerField(null=True)
    des = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Contact(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    subject = models.CharField(max_length=100, null=True)
    message = models.TextField(blank=False, null=True)

    def __str__(self):
        if self.name == None:
            return "-"
        return self.name


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery', null=True)
    desc = models.CharField(max_length=300, null=True)

    def __str__(self):
        if self.desc == None:
            return "-"
        return self.desc
