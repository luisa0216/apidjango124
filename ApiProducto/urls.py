from rest_framework import routers
from .api import ProductoviewSet

router= routers.DefaultRouter()
router.register('api/ApiProducto', ProductoviewSet, 'ApiProducto')

urlpatterns = router.urls