from django.urls import path
from addresses.views import AddressView, AddressDetailView

urlpatterns = [
    path("address/", AddressView.as_view()),
    path("address/<int:user_id>", AddressDetailView.as_view()),
]