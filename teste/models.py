from django.db import models

class Humano(models.Model):
    texto_pensamento = models.TextField(blank=True, null=True)
    texto_sonho = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.texto_pensamento:
            return f"Pensamento: {self.texto_pensamento[:20]}"  # Exibe os primeiros 20 caracteres do pensamento
        if self.texto_sonho:
            return f"Sonho: {self.texto_sonho[:20]}"  # Exibe os primeiros 20 caracteres do sonho
        return "Sem texto"