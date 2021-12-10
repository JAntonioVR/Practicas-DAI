#
# ──────────────────────────────────────────────────────────────────────────────────
#   :::::: mi_sitio/urls.py : :  :   :    :     :        :          :
# ──────────────────────────────────────────────────────────────────────────────────
#


# ─── IMPORTS ────────────────────────────────────────────────────────────────────
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

# ─── URLS ───────────────────────────────────────────────────────────────────────
urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include('galerias.urls')),
]

# ─── MEDIA ──────────────────────────────────────────────────────────────────────
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
