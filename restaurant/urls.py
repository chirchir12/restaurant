from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
# from django.contrib.auth.views import logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('menu.urls') ),
    path("",include("accounts.urls")),
    path("",include("social_django.urls",namespace='social')),
    # path("logout/",logout,{"next_page":settings.LOGOUT_REDIRECT_URL},name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
