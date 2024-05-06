from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import index
from .views import BookingViewSet, MenuItemView, MenuItemDetailView

router = DefaultRouter()
router.register('bookings', BookingViewSet, basename='bookings')

urlpatterns = [
    # path('bookings/', BookingView.as_view(), name='bookings'),
    path('', index, name='index'),
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('menu/', MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>/', MenuItemDetailView.as_view(), name='menu-detail'),
]