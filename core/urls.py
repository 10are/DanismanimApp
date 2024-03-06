from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings  
from django.conf.urls.static import static

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
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('client/', include('client.urls')),  
    path('counselor/', include('counselor.urls')),  
    path('blog/', include('blog.urls')),
    path('randevu/', include('appointment.urls')),
    path('transaction/', include('transaction.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
