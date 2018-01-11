# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.shortcuts import redirect
from grconst.apps.site_content.models import Service, PortfolioItem, AboutDate, TeamItem
from grconst.apps.site_content.forms import MessageForm

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

class MessageProcessView(View):
    def post(self, request, *args, **kwargs):
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['contact_error'] = False
            request.session['contact_message'] = 'Your message has been sent. Somebody will be in contact with you'
        else: 
            request.session['contact_error'] = True
            request.session['contact_message'] = 'There was an error saving your message. Please make sure everything is correct and try again.'

        return redirect('/#contact')
