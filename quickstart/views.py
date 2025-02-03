from .models import Pemain, Klub, Mahasiswa
from rest_framework import generics
from .serializer import PemainSerializer, KlubSerializer, MahasiswaSerializer



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


# Mahasiswa API Views
class MahasiswaList(generics.ListAPIView):
    queryset = Mahasiswa.objects.all()
    serializer_class = MahasiswaSerializer

class MahasiswaCreate(generics.CreateAPIView):
    queryset = Mahasiswa.objects.all()
    serializer_class = MahasiswaSerializer

class MahasiswaDetail(generics.RetrieveAPIView):
    queryset = Mahasiswa.objects.all()
    serializer_class = MahasiswaSerializer

class MahasiswaUpdate(generics.UpdateAPIView):
    queryset = Mahasiswa.objects.all()
    serializer_class = MahasiswaSerializer

class MahasiswaDelete(generics.DestroyAPIView):
    queryset = Mahasiswa.objects.all()
    serializer_class = MahasiswaSerializer



