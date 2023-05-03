from django.urls import path

from . import views

urlpatterns = [
    path('cart/', views.AddToCartView.as_view()),
    path('cart/<int:product_id>/', views.CartDetailView.as_view()),
    # path('cart/clear/', views.CartDetailView.as_view()),
]