from django.conf.urls import patterns, include, url
from AKPsiWebsite.views import *

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'AKPsiWebsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # home page
    url(r'^$', index_view),

    # about us page
    url(r'^about/$', about_view),

    # brothers page
    url(r'^brothers/$', brothers_view),

    # news page
    url(r'^news/$', news_view),

    # recruitment page
    url(r'^recruitment/$', recruitment_view),

    # sign up page
    url(r'^signup/$', signup_view),

    # application page
    url(r'^application/$', application_view),

    # logout page
    url(r'^logout/$', logout_view),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
