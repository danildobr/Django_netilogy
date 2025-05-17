from django.urls import path
from django.contrib import admin
from calculator.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('omlet/', omlet, name='omlet'),
    path('pasta/', pasta, name='pasta'),
    path('buter/', buter, name='buter'),
]