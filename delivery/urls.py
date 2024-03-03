from django.urls import path
from . import views

urlpatterns = [
    path('start-delivery/', views.start_delivery, name='start-delivery'),
    path('active-delivery/', views.active_delivery, name='active-delivery'),
    path('delivery-history/', views.delivery_history, name='delivery-history'),
    path('assign-delivery/<int:pk>/', views.assign_delivery, name='assign-delivery'),
    path('delivery-queue/', views.delivery_queue, name='delivery-queue'),
    path('rider-queue/', views.rider_queue, name='rider-queue'),
    path('complete-delivery/<int:pk>/', views.complete_delivery, name='complete-delivery')
]