from django.urls import path
from addresses.views import AddressView, AddressDetailView

urlpatterns = [
    path("addresses/", AddressView.as_view()),
    path("addresses/<int:user_id>/", AddressDetailView.as_view()),
]