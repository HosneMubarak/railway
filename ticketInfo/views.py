from django.shortcuts import render
import json

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import TicketInfo, Booking
from .serializers import TicketInfoSerializer, BookingSerializer, UserBookedSerializer
from rest_framework.exceptions import ValidationError


class TicketInfoView(APIView):
    """ Retrieve all train schedute."""
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        ticket_info_query = TicketInfo.objects.all()
        serializer = TicketInfoSerializer(ticket_info_query, many=True)
        return Response(serializer.data)


class UserTicketInfoView(APIView):
    """ Retrieve all train schedute."""
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        current_user_id = request.user.id
        ticket_info_query = Booking.objects.filter(user__id=current_user_id)
        context = {

        }
        serializer = UserBookedSerializer(ticket_info_query, many=True)
        return Response(serializer.data)


class BookingView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        # getting ticket currect_data
        ticket = TicketInfo.objects.get(id=request.data['ticket'])
        print(ticket.seat)
        # assign new seat availabe
        new_seat_availabe = int(ticket.seat) - 1
        print(new_seat_availabe)
        if ticket.seat != 0:
            if serializer.is_valid():
                serializer.save()
                TicketInfo.objects.filter(id=request.data['ticket']).update(seat=new_seat_availabe)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            raise ValidationError({'error': 'Sorry ticket not availabe'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
