from django.db import models
from django.core.validators import MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField

class Room(models.Model):
    room_name = models.CharField(max_length=100, verbose_name="Room Name")
    room_pictures = models.ImageField(upload_to='static/images/room_pictures', verbose_name="Room Pictures")
    card_description = models.CharField(max_length=255, verbose_name="Card Description")
    room_description = models.TextField(verbose_name="Room Description")

    def __str__(self):
        return self.room_name

class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to='static/images/room_pictures', verbose_name="Room Pictures")

    def __str__(self):
        return self.room.room_name                             
    
class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name="Reserved Room")
    check_in = models.DateField(verbose_name="Check-in Date")
    check_out = models.DateField(verbose_name="Check-out Date")
    guest_name = models.CharField(max_length=100, verbose_name="Guest Name")
    guest_email = models.EmailField(verbose_name="Guest Email")
    guest_phone = PhoneNumberField(blank=True, null=True, verbose_name="Guest Phone")
    num_guests = models.IntegerField(default=1, validators=[MaxValueValidator(2)], verbose_name="Number of Guests")
    dog = models.BooleanField(default=False, blank=True, null=True, verbose_name="Dog")
    vehicle = models.BooleanField(default=False, verbose_name="Vehicle")
    guest_info = models.TextField(blank=True, null=True, verbose_name="Additional Information")
    reservation_date = models.DateTimeField(auto_now_add=True, verbose_name="Reservation Date")    
    reservation_status = models.BooleanField(default=False, verbose_name="Reservation Status")
    
    def __str__(self):
        return self.guest_name
