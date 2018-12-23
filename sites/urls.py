from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sites/(\d+)', views.project, name='project'),
    url(r'^upload/$', views.upload_site, name='upload'),
    url(r'^profile/(?P<username>\w{0,50})/$', views.profile, name='profile'),
    url(r'^search/$', views.search, name='search_results'),
    # url(r'^new_review/$', views.new_review, name='new_review')
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)