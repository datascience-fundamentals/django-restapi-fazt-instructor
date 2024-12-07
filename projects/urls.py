from rest_framework import routers
from .api import ProjectViewSet
# trailing_slash -> We modify this attribute to avoid slash auto appaned on urls
router = routers.DefaultRouter(trailing_slash="")
router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = router.urls
