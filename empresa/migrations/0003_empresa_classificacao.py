# Generated by Django 4.2.16 on 2024-11-19 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0002_empresa_delete_formulario'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='classificacao',
            field=models.CharField(default='default_value', max_length=100),
        ),
    ]
