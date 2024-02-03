# Ana projenizin urls.py dosyası

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Danismanim API",
        default_version='v1',
        description="açıklama gelebilir",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('client/', include('client.urls')),  
    path('counselor/', include('counselor.urls')),  
    path('blog/', include('blog.urls')), 
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
]
