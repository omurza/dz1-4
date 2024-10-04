from django.urls import path
from settings.views import settings, eshkere

urlpatterns = [
    path('', settings, name="settings"),
    path('eshkere/', eshkere, name="eshkere"),  #
]
