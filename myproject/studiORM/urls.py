from django.urls import path
from . import views

urlpatterns = [
    path('statistics/', views.statistics_view, name='statistics'),  # Pastikan ini ada
    # Tambahkan pola URL lainnya di sini jika perlu
]
