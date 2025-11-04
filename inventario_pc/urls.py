from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', lambda request: render(request, 'index.html')),  # 👈 esta línea debe estar así
    path('admin/', admin.site.urls),
    path('', include('computadoras.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
