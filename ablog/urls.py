from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "My Freakin' Awesome Blog! Admin"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "Welcome to My Freakin' Awesome Blog! Admin Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('theblog.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
