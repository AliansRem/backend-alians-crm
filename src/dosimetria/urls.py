from rest_framework.routers import DefaultRouter

from dosimetria import views

router = DefaultRouter()

routes = {
    'client': views.ClientAPI,
    'quarter': views.QuarterAPI,
    'contract': views.ContractAPI,
    'contact': views.ContactAPI,
    'actual-address': views.ActualAddressAPI,
    'invoice': views.InvoiceAPI,
    'protocol': views.ProtocolAPI,
    'transmitted-document': views.TransmittedDocumentAPI
}

for prefix, api in routes.items():
    router.register(prefix, api)

urlpatterns = router.urls
