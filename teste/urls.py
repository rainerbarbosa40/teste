from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views  # Importar views é suficiente, não precisa importar `registrar_humano` separadamente

urlpatterns = [
    path('', views.index, name='index'),
    path('registrar/', views.registrar_humano, name='registrar_humano'),

    # Outros padrões de URL
]

# Adicione esta linha para servir arquivos estáticos durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
