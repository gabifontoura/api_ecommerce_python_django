from django.urls import path

from orders.views import OrderView, OrderDetailView, OrderSoldView, OrderFinishedView

urlpatterns = [
    path('orders/', OrderView.as_view()),
    path('orders/<int:order_id>/', OrderDetailView.as_view()),
    path('orders/sold/<int:user_id>/', OrderSoldView.as_view()),
    path('orders/finished/<int:user_id>/', OrderFinishedView.as_view()),
]