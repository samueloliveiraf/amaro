# Generated by Django 4.0.5 on 2022-06-21 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0002_alter_imoveis_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='imoveis',
            name='imagens',
            field=models.ImageField(default=1, upload_to='images'),
            preserve_default=False,
        ),
    ]
