from django.contrib import admin
from django.urls import path
from main import views  # AJOUTE CETTE LIGNE
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),  # AJOUTE CETTE LIGNE
]





if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
