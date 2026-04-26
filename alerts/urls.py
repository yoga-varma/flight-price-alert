from django.urls import path
from .views import (
    CreateAlertView, ListAlertView, DeleteAlertView,
    CreateRouteView, ListRouteView,
    CreatePriceSnapshotView, ListPriceSnapshotView
)

urlpatterns = [
    path('alerts/', CreateAlertView.as_view()),
    path('alerts/list/', ListAlertView.as_view()),
    path('alerts/<int:pk>/', DeleteAlertView.as_view()),

    path('routes/', CreateRouteView.as_view()),
    path('routes/list/', ListRouteView.as_view()),

    path('prices/', CreatePriceSnapshotView.as_view()),
    path('prices/list/', ListPriceSnapshotView.as_view()),
]