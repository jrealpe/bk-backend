from django.conf.urls import include, url

from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'user', ProductViewSet, base_name='user')

urlpatterns = [
	url(r'^/', include(router.urls)),
]
