from django.urls import path
from .views import TicketInfoView, BookingView, UserTicketInfoView
urlpatterns = [
    path('all_train_scedule/', TicketInfoView.as_view(), name='schedule'),
    path('user_ticket/', UserTicketInfoView.as_view(), name='user-ticket'),
    path('ticket_booking/', BookingView.as_view(), name='booking'),
]