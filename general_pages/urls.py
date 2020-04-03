from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('terms-of-service', views.TosView.as_view(), name='tos'),
    path('privacy-policy', views.PrivacyPolicyView.as_view(), name='privacy'),
]