# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import ModelForm
from grconst.apps.site_content.models import Message

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'phone', 'message']
