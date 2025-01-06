from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.apps.portfolio.views.portfolio import (
    CategoryView,
    PortfolioView,
    SkilsView,
    ResumeView,
)
from core.apps.portfolio.views import ContactView, BaseskilsView


router = DefaultRouter()
router.register(r"category", CategoryView, basename='category')
router.register(r"portfolio", PortfolioView, basename='portfolio')
router.register(r"skils", SkilsView, basename='skils')
router.register(r"resume", ResumeView, basename='resume')
router.register(r"contact", ContactView, basename='contact')
router.register(r"baseskils", BaseskilsView, basename='baseskils')





urlpatterns = [
    path("", include(router.urls)),
]
