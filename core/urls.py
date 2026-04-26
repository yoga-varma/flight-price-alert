from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


def home(request):
    return JsonResponse({
        "message": "Flight Price Alert API is running successfully",
        "endpoints": {
            "admin": "/admin/",
            "api": "/api/",
            "token": "/api/token/",
            "refresh_token": "/api/token/refresh/"
        }
    })


urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),
    path("api/", include("alerts.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]