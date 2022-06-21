from django.db import models


TIPO_CHOICES = (
    ("1", "CASA"),
    ("2", "TERRENO"),
    ("3", "APARTAMENTO")
)


class ImagemImoveis(models.Model):
    imagem = models.FileField(upload_to='images_imoveis/')

    class Meta:
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'
        ordering = ['-id']

        db_table = 'imagens_imoveis'

    def __str__(self):
        return f'{self.imagem}'


class Imoveis(models.Model):
    nome_cabecalho = models.CharField(max_length=150, blank=True, null=True)
    tipo = models.CharField(max_length=150, choices=TIPO_CHOICES, blank=True, null=True)
    imagens = models.ManyToManyField(ImagemImoveis)

    class Meta:
        verbose_name = 'Imovel'
        verbose_name_plural = 'Imoveis'
        ordering = ['-id']

        db_table = 'imoveis'

    def __str__(self):
        return f'{self.id}|{self.nome_cabecalho}'
