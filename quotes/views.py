from rest_framework import viewsets
from .models import Personality
from .serializers import *

# Create your views here.
class PersonalityViewSet(viewsets.ModelViewSet):
    """ViewSet for abstraction of List and detail views of Personality model"""

    queryset = Personality.objects.all().order_by("id")
    serializer_class = PersonalitySerializer
