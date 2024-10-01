from django.contrib import admin
from django.urls import include, path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="API test Project",
        default_version='v1',
        description="API documentation for the api test project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="shokoohrigi22@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=([permissions.AllowAny]),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('estimate/', include('estimate.urls')),
    path('management/', include('management.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
