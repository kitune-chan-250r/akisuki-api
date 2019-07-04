
# Create your views here.
from rest_framework import viewsets

from .models import Count_data
from .serializer import CountDataSerializer


class CountDataViewSet(viewsets.ModelViewSet):
    queryset = Count_data.objects.all()
    serializer_class = CountDataSerializer
