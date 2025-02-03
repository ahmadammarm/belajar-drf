from rest_framework import serializers
from .models import Pemain, Klub, Mahasiswa


# Mengubah data menjadi format JSON
class KlubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klub
        fields = ['id', 'nama', 'negara', 'stadion']



class PemainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pemain
        fields = ['id', 'nama', 'umur', 'posisi', 'negara']

class MahasiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahasiswa
        fields = ['id', 'nama', 'nim', 'prodi', 'fakultas']


