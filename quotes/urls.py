from django.urls import include, path
from rest_framework import routers
from quotes import views

router = routers.DefaultRouter()
router.register(r"personality", views.PersonalityViewSet)

urlpatterns = [path("", include(router.urls))]
