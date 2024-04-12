from django.urls import path
from .views import index
from .views import BookingView, MenuView

urlpatterns = [
    path('', index, name='index'),
    path('api/bookings/', BookingView.as_view(), name='bookings'),
    path('api/menu/', MenuView.as_view(), name='menu'),
]