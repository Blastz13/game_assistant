from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from ninja import NinjaAPI

from user.views import user_router
from assistant.views import assistant_router

api = NinjaAPI()

api.add_router('/users/', user_router)
api.add_router('/assistant/', assistant_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
