from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http.response import HttpResponse
from django.views.static import serve as static_serve
from django_nyt.urls import get_pattern as get_notify_pattern
from wiki.urls import get_pattern as get_wiki_pattern
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^robots.txt', lambda _: HttpResponse('User-agent: *\nDisallow: /')),
    url(r'^robots.txt$', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="project_robots_file"),
    url(r'^dictapp/', include('dictapp.urls')),
    url(r'^bookapp/', include('bookapp.urls')),
    # url(r'^backing/', include('backing.urls')),
    # url(r'^blogapp/', include('blogapp.urls')),
    url(r'', include('introapp.urls')),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', static_serve, {'document_root': settings.MEDIA_ROOT}),
    ]


urlpatterns += [
    url(r'^notify/', get_notify_pattern()),
    url(r'^wiki/', get_wiki_pattern())
]

handler500 = 'wiki_site.views.server_error'
handler404 = 'wiki_site.views.page_not_found'
