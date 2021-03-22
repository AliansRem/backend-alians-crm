from rest_framework.routers import DefaultRouter

from core import views

router = DefaultRouter()

routes = {
    'client': views.ClientAPI,
    'contact': views.ContactAPI,
}

for prefix, api in routes.items():
    router.register(prefix, api)

urlpatterns = router.urls
