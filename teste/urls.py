from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pensamentos/', views.pensamentos, name='pensamentos'),
]
    # Outros padrões de URL

# Adicione esta linha para servir arquivos estáticos durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

