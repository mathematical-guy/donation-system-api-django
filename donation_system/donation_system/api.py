from rest_framework.routers import DefaultRouter
from payment_app.views import DonationViewSet


router = DefaultRouter()
router.register('donations', DonationViewSet, basename="donations")


urlpatterns = router.urls
