from django.conf.urls import url, patterns, include
from django.conf import settings
from django.contrib import admin

from tourbus.views import http_404, http_500

admin.autodiscover()

handler404 = http_404
handler500 = http_500

urlpatterns = patterns(
    '',
    (r'^manageme/', include(admin.site.urls)),
    (r'^grappelli/', include('grappelli.urls')),
    #(r'^ckeditor/', include('ckeditor.urls')),
    #(r'^flatblocks/', include('flatblocks.urls')),
    #(r'^markitup/', include('markitup.urls')),

    #(r'^core/', include('{{ project_name }}.core.urls')),
)

# serving user-uploaded files within development env
if settings.DEBUG:
    urlpatterns += patterns(
        '',
        (r'^{0}(?P<path>.*)$'.format(settings.MEDIA_URL[1:]),
         'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}))
