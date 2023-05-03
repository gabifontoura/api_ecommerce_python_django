from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView

# from users.permissions import IsAccountOwner
from addresses.models import Address
from addresses.serializers import AddressSerializer

# Create your views here.
class AddressView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsLogged]

    serializer_class = AddressSerializer
    queryset = Address.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AddressDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsOwner]

    serializer_class = AddressSerializer
    lookup_field = "user_id"

    def get_queryset(self):
        return Address.objects.filter(user_id = self.kwargs[self.lookup_field])
