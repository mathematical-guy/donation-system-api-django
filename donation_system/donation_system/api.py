from django.urls import path
from rest_framework.routers import DefaultRouter
from payment_app.views import DonationViewSet
from account_management.views import DonationReceiversListView, UserLoginView, UserSignUpView

router = DefaultRouter()
router.register('donations', DonationViewSet, basename="donations")


urlpatterns = [
    path('login/', UserLoginView.as_view()),
    path('donation-receivers/', DonationReceiversListView.as_view()),
    path('sign-up/', UserSignUpView.as_view()),
]


urlpatterns += router.urls
