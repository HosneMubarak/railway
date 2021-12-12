from django.contrib.auth.models import User
from django.db import models
import datetime


# Create your models here.
class TicketInfo(models.Model):
    """Ticket information"""
    name = models.CharField(max_length=255, null=True, blank=True)
    to_station = models.CharField(max_length=255, null=True, blank=True)
    from_station = models.CharField(max_length=255, null=True, blank=True)
    date = models.CharField(max_length=255, null=True, blank=True)
    time = models.CharField(max_length=255, null=True, blank=True)
    seat_class = models.CharField(max_length=255, null=True, blank=True)
    route = models.CharField(max_length=255, null=True, blank=True)
    seat = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} From {self.from_station} to {self.to_station}"


class Booking(models.Model):
    """Create Booking"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(TicketInfo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.ticket.name} - f{self.ticket.time}- f{self.ticket.price}"
