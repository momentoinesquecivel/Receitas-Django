# Generated by Django 3.2.3 on 2021-06-14 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0004_receita_foto_receita'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='foto_receita',
            field=models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d'),
        ),
    ]