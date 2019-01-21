from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('test', views.TestView)
router.register('as', views.ASView)


urlpatterns = [
    url(r'', include(router.urls)),
]