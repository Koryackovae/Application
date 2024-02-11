from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from web.views import tags_view

urlpatterns = [
    path('', include('web.urls')),
    path('admin/', admin.site.urls),
    path("tags/",tags_view, name="")
]

if settings.DEBUD:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
