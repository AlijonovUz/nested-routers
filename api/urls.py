from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter

from .views import GroupViewSet, ChapterViewSet

router = DefaultRouter()
router.register(r'my-groups', GroupViewSet)

chapters = NestedSimpleRouter(router, r'my-groups', lookup='group')
chapters.register(r'chapters', ChapterViewSet, basename='group-chapters')

urlpatterns = []
urlpatterns.extend(router.urls)
urlpatterns.extend(chapters.urls)