from .views import *
from django.urls import path


urlpatterns = [
    path('orders/', ListOrdersView.as_view(), name='order'),
    path('orders/<int:id>', DetailOrderView.as_view()),
    path('orders/<int:id>/delete', RemoveOrderView.as_view()),
    path('orders/create_order', CreateOrderAPIView.as_view()),
]


