# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView
from grconst.apps.site_content.views import IndexView, MessageProcessView
from grconst.sitemaps import StaticViewSitemap

urlpatterns = [
    url(r'^googlee127aae73e8dcd95\.html$', TemplateView.as_view(template_name='googlee127aae73e8dcd95.html')),
    url(r'^sitemap\.xml$', sitemap, 
        {'sitemaps': {
            'static': StaticViewSitemap
            }
        },
        name='django.contrib.sitemaps.views.sitemap'),
    url(r'^post-message/', MessageProcessView.as_view(), name='message-process'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(), name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
