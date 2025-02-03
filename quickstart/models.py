from django.db import models



# Membuat moddel yang akan dijadikan sebagai entitas database
class Pemain(models.Model):
    nama = models.CharField(max_length=100)
    umur = models.IntegerField()
    posisi = models.CharField(max_length=50)
    negara = models.CharField(max_length=50)

    def __str__(self):
        return self.nama


class Klub(models.Model):
    nama = models.CharField(max_length=100)
    negara = models.CharField(max_length=50)
    stadion = models.CharField(max_length=50)

    def __str__(self):
        return self.nama

class Mahasiswa(models.Model):
    nama = models.CharField(max_length=100)
    nim = models.CharField(max_length=100, unique=True)
    prodi = models.CharField(max_length=100)
    fakultas = models.CharField(max_length=100)

    def __str__(self):
        return self.nama

