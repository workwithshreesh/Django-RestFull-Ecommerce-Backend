from django.urls import path
from returnscustomer.views import ReturnedRequestView

urlpatterns = [
    path("returned-request/", ReturnedRequestView.as_view(), name="returnedrequest"),
    path("returned-request/<int:pk>", ReturnedRequestView.as_view(), name="returnedrequest"),

]