"""
Last modification: 02/06/2022
Created: 02/06/2022
Author Rodrigo Carmona Mendoza
Supported by lidisen.com
"""

"""Home views"""

# Django
from django.views.generic import TemplateView
from django.shortcuts import render


# Local home class view
class homeClass(TemplateView):
    template_name = 'home/landing.html'

    def get_context_data(self, **kwargs):
        context = super(homeClass, self).get_context_data(**kwargs)
        context['landing'] = True
        return context
