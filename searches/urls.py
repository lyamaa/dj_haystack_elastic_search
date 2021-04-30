from django.urls.conf import include, path
from rest_framework.routers import DefaultRouter

from .views import LocationSearchView

router = DefaultRouter()
router.register(r"location/search", LocationSearchView, basename="location-search")

urlpatterns = router.urls
