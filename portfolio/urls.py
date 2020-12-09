from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns=[
    url('^$',views.index,name = 'index'),
    url('about/', views.about, name='about'),
    url('projects/', views.projects, name='projects'),
    url('contacts/', views.contacts, name='contacts'),
    ]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)