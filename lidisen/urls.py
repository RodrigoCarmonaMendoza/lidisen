"""
Last modification: 26/04/2022
Created: 04/26/2022
Author Rodrigo Carmona Mendoza
Supported by lidisen.com
"""

"""lidisen URL Configuration URLs module. """

# Django
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    # Django urls
    path('admin/', admin.site.urls),

    # Local urls
    path('', include(('home.urls', 'home'), namespace='home')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)