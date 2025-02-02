from django.urls import path
from .views import PemainCreate, PemainDelete, PemainDetail, PemainList, PemainUpdate, KlubList, KlubCreate, KlubDelete, KlubDetail, KlubUpdate


# Tidak menggunakan /pemain lagi karena sudah didefinisikan di base urlnya
urlpatterns = [
    
    # Klub Endpoint
    path('', KlubList.as_view(), name='klub-list'),
    path('create', KlubCreate.as_view(), name='klub-create'),
    path('<int:pk>', KlubDetail.as_view(), name='klub-detail'),
    path('update/<int:pk>', KlubUpdate.as_view(), name='klub-update'),
    path('delete/<int:pk>', KlubDelete.as_view(), name='klub-delete'),


    # Pemail Endpoint
    path('', PemainList.as_view(), name='pemain-list'),
    path('create', PemainCreate.as_view(), name='pemain-create'),
    path('<int:pk>', PemainDetail.as_view(), name='pemain-detail'),
    path('update/<int:pk>', PemainUpdate.as_view(), name='pemain-update'),
    path('delete/<int:pk>', PemainDelete.as_view(), name='pemain-delete'),
]
