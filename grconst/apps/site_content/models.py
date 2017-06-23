# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Service(models.Model):
    """Service Model"""
    fa_icon_str = models.CharField(max_length=215, blank=True, null=True)
    image_file = models.FileField(upload_to='services/icons/', blank=True, null=True)
    title = models.CharField(max_length=215, default='Title')
    description = models.TextField(default='Description')

class PortfolioItem(models.Model):
    """Portfolio Item"""
    thumbnail = models.FileField(upload_to='portfolio/thumbnails')
    title = models.CharField(max_length=512, default='Title')
    subtitle = models.CharField(max_length=512, default='Sub Title')
    description = models.TextField(default='Description')

class PortfolioImage(models.Model):
    """Portfolio Image"""
    image_file = models.FileField(upload_to='portfolio/images')
    portfolio = models.ForeignKey(PortfolioItem, related_name='images')

class AboutDate(models.Model):
    """About Date"""
    image_file = models.FileField(upload_to='about/images')
    date_range = models.CharField(max_length=215, default='2010=2017')
    title = models.CharField(max_length=215, default='Title')
    description = models.TextField(default='Description')

class TeamItem(models.Model):
    """Team Item"""
    image_file = models.FileField(upload_to='about/images')
    title = models.CharField(max_length=215, default='Title')
    subtitle = models.CharField(max_length=215, default='Subtitle')
    twitter = models.CharField(max_length=1024, default='http://twitter.com')
    facebook = models.CharField(max_length=1024, default='http://facebook.com')
    linkedin = models.CharField(max_length=1024, default='http://linkedin.com')
