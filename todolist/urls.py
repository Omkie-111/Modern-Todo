from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework.authentication import BasicAuthentication

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
]

rest_framework_default_authentication_classes = [
    BasicAuthentication,
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
