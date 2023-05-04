from django.urls import path

from . import views

urlpatterns = [
    path('carts/', views.AddToCartView.as_view()),
    path('carts/my_cart/', views.ListCartView.as_view()),
    path('carts/<int:product_id>/', views.CartDetailView.as_view()),
]