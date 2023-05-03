from django.urls import path

from . import views

urlpatterns = [
    path('cart/', views.AddToCartView.as_view()),
    path('cart/<int:product_id>/', views.RemoveFromCartView.as_view()),
]