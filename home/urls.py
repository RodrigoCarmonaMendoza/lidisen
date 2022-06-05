"""
Last modification: 04/27/2022
Created: 04/27/2022
Author Rodrigo Carmona Mendoza
Supported by lidisen.com
"""

"""Home URLs"""

# Django
from django.urls import path

# Views
from home.views import homeClass

# Local urls
urlpatterns = [

    path(
        route='',
        view=homeClass.as_view(),
        name='home'
    ),

]
