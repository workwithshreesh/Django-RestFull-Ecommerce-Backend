from django.urls import path
from returnscustomer.views import ReturnedRequestView, ReturnedProduct

urlpatterns = [
    path("returned-request/", ReturnedRequestView.as_view(), name="returnedrequest"),
    path("returned-request/<int:pk>", ReturnedRequestView.as_view(), name="returnedrequest"),
    path("returned-product/",ReturnedProduct.as_view(), name="returnedproduct"),
    path("returned-product/<int:pk>",ReturnedProduct.as_view(), name="returnedproductid"),
]