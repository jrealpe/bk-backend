from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from apps.catalogue import urls as catalogue_urls
from apps.customer import views as customer_views
from apps.customer.viewsets import CustomObtainAuthToken


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Auth
    url(r'^api/login/', CustomObtainAuthToken.as_view()),
    url(r'^api/signup/', customer_views.sign_up),

    # API
    url(r'^api/catalogue', include(catalogue_urls)),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
