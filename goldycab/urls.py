from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Goldy Cab Services Admin Portal"
admin.site.site_title = "Goldy Cab Admin Portal"
admin.site.index_title = "Welcome to Goldy Cab Services Portal"
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("bookings.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
