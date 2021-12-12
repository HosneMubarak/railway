from rest_framework import serializers
from .models import TicketInfo, Booking


class TicketInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketInfo
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"


class UserBookedSerializer(serializers.ModelSerializer):
    ticket = TicketInfoSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = "__all__"
