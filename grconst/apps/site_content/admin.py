# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from grconst.apps.site_content.models import (Service, PortfolioItem, PortfolioImage,
                                             AboutDate, TeamItem)
# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    pass
class PortfolioItemAdmin(admin.ModelAdmin):
    pass
class PortfolioImageAdmin(admin.ModelAdmin):
    pass
class AboutDateAdmin(admin.ModelAdmin):
    pass
class TeamItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(Service, ServiceAdmin)
admin.site.register(PortfolioItem, PortfolioItemAdmin)
admin.site.register(PortfolioImage, PortfolioImageAdmin)
admin.site.register(AboutDate, AboutDateAdmin)
admin.site.register(TeamItem, TeamItemAdmin)
