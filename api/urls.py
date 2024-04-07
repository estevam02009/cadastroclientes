from rest_framework.routers import DefaultRouter
from api.views import CadastroClienteViewSet

app_name = 'api'

router = DefaultRouter(trailing_slash=False)
router.register(r'cadastros', CadastroClienteViewSet)

urlpatterns = router.urls