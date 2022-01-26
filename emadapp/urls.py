from django.urls import path
from emadapp.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home')
]
