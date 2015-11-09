from django.conf.urls import patterns, include, url
from books import views
import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    # Example:
    # (r'^BookDB/', include('BookDB.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/', include(admin.site.urls)),
    (r'^$', views.home),
    (r'^index/$', views.home),
    (r'^detail/$', views.detail),
    (r'^change/$', views.change),
    (r'^delete/$', views.delbook),
    (r'^search/$', views.search),
    (r'^book/$', views.newbook),
    (r'^author/$', views.newauthor),
)
