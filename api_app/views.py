from .models import AppleCeo
from rest_framework import viewsets

# from rest_framework import permissions
from .serializers import AppleCeoSerializer


# Create your views here.
class CeoViewSet(viewsets.ModelViewSet):
    queryset = AppleCeo.objects.all().order_by("-year_started")
    serializer_class = AppleCeoSerializer
