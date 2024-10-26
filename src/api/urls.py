from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import AuthorViewSet, BookViewSet, TagViewSet

app_name = "api"

router_v1 = DefaultRouter()

router_v1.register(r"author", AuthorViewSet, basename="author")
router_v1.register(r"book", BookViewSet, basename="book")
router_v1.register(r"tag", TagViewSet, basename="tag")


urlpatterns = [
    path("", include(router_v1.urls)),
]
