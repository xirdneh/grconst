# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from grconst.apps.site_content.models import Service, PortfolioItem, AboutDate, TeamItem

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        context['portfolio_items'] = PortfolioItem.objects.all()
        context['about_dates'] = AboutDate.objects.all()
        context['team_items'] = TeamItem.objects.all()
        return context
