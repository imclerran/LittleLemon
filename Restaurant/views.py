from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking, MenuItem
from .serializers import BookingSerializer, MenuItemSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class BookingView(APIView):
    
    def get(self, request):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response({"bookings": serializer.data})
    
    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "Booking created successfully", "status": "success", "data": serializer.data}, status=201)
    
class MenuView(APIView):
    
    def get(self, request):
        menus = MenuItem.objects.all()
        serializer = MenuSerializer(menus, many=True)
        return Response({"menus": serializer.data})
    
    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "MenuItem created successfully", "status": "success", "data": serializer.data}, status=201)

# class BookingViewSet(viewsets.ModelViewSet):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer

# class MenuViewSet(viewsets.ModelViewSet):
#     queryset = Menu.objects.all()
#     serializer_class = MenuSerializer