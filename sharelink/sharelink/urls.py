from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from sharelink.linkhome.views import index, add_link, crawer

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sharelink.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^newlink/$', add_link),
    url(r'^crawer/$', crawer),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
