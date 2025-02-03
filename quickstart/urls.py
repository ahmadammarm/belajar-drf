from django.urls import path
from .views import PemainCreate, PemainDelete, PemainDetail, PemainList, PemainUpdate, KlubList, KlubCreate, KlubDelete, KlubDetail, KlubUpdate, MahasiswaList, MahasiswaCreate, MahasiswaDetail, MahasiswaUpdate, MahasiswaDelete


# Tidak menggunakan /pemain lagi karena sudah didefinisikan di base urlnya
urlpatterns = [

    # Klub Endpoint
    path('klub-list', KlubList.as_view(), name='klub-list'),
    path('create-klub', KlubCreate.as_view(), name='klub-create'),
    path('klub-detail/<int:pk>', KlubDetail.as_view(), name='klub-detail'),
    path('klub-update/<int:pk>', KlubUpdate.as_view(), name='klub-update'),
    path('klub-delete/<int:pk>', KlubDelete.as_view(), name='klub-delete'),


    # Pemail Endpoint
    path('pemain-list', PemainList.as_view(), name='pemain-list'),
    path('create-pemain', PemainCreate.as_view(), name='pemain-create'),
    path('pemain-detail/<int:pk>', PemainDetail.as_view(), name='pemain-detail'),
    path('pemain-update/<int:pk>', PemainUpdate.as_view(), name='pemain-update'),
    path('pemain-delete/<int:pk>', PemainDelete.as_view(), name='pemain-delete'),

    # Mahasiswa Endpoint
    path('mahasiswa-list', MahasiswaList.as_view(), name = 'mahasiswa-list'),
    path('create-mahasiswa', MahasiswaCreate.as_view(), name = 'mahasiswa-create'),
    path('mahasiswa-detail/<int:pk>', MahasiswaDetail.as_view(), name = 'mahasiswa-detail'),
    path('mahasiswa-update/<int:pk>', MahasiswaUpdate.as_view(), name = 'mahasiswa-update'),
    path('mahasiswa-delete/<int:pk>', MahasiswaDelete.as_view(), name = 'mahasiswa-delete')
]
