from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from apps.catalogue import urls as catalogue_urls


from .views import index, SignOutView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^incia-sesion/$', index, name='index'),
    url(r'^cerrar-sesion/$', SignOutView.as_view(), name='sign_out'),

    # API
    url(r'^api/catalogue', include(catalogue_urls)),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
