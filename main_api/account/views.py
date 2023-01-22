from rest_framework.viewsets import ModelViewSet
from .models import UserProfile
from .serializers import AccountSerializer

# Create your views here.
class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = AccountSerializer
    