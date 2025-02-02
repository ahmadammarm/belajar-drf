from .models import Pemain, Klub
from rest_framework import generics
from .serializer import PemainSerializer, KlubSerializer



# Pemain API Views
class PemainCreate(generics.CreateAPIView):
    queryset = Pemain.objects.all()
    serializer_class = PemainSerializer

class PemainList(generics.ListAPIView):
    queryset = Pemain.objects.all()
    serializer_class = PemainSerializer

class PemainDetail(generics.RetrieveAPIView):
    queryset = Pemain.objects.all()
    serializer_class = PemainSerializer

class PemainUpdate(generics.UpdateAPIView):
    queryset = Pemain.objects.all()
    serializer_class = PemainSerializer

class PemainDelete(generics.DestroyAPIView):
    queryset = Pemain.objects.all()
    serializer_class = PemainSerializer


# Klub API Views
class KlubCreate(generics.CreateAPIView):
    queryset = Klub.objects.all()
    serializer_class = KlubSerializer

class KlubList(generics.ListAPIView):
    queryset = Klub.objects.all()
    serializer_class = KlubSerializer

class KlubDetail(generics.RetrieveAPIView):
    queryset = Klub.objects.all()
    serializer_class = KlubSerializer

class KlubUpdate(generics.UpdateAPIView):
    queryset = Klub.objects.all()
    serializer_class = KlubSerializer

class KlubDelete(generics.DestroyAPIView):
    queryset = Klub.objects.all()
    serializer_class = KlubSerializer




