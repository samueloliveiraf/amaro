from django.contrib import admin
from .models import Imoveis, ImagemImoveis


admin.site.register(
    [
        Imoveis,
        ImagemImoveis
    ]
)
