from django.urls import path
from .views import index
from .views import BookingView, MenuView

urlpatterns = [
    path('bookings/', BookingView.as_view(), name='bookings'),
    path('menu/', MenuView.as_view(), name='menu'),
]