from django.shortcuts import get_object_or_404

from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Musician
from .serializers import ChartSerializer


class ChartLook(ListAPIView):
    serializer_class = ChartSerializer
    queryset = Musician.objects.all()


class SongLook(RetrieveAPIView):
    serializer_class = ChartSerializer

    def get_object(self):
        return get_object_or_404(Musician, author=self.kwargs['author'])
