from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from teste.views import index

urlpatterns = [
    path('', index, name='index'),
    # Outros padrões de URL
]

# Adicione esta linha para servir arquivos estáticos durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
