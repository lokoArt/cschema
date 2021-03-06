from django.conf.urls import url, include
from rest_framework import routers
from insurance import views

router = routers.DefaultRouter()
router.register(r'schemas', views.ReadSchemaViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]