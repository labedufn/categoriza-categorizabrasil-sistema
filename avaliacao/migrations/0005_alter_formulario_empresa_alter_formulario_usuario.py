# Generated by Django 4.2.16 on 2024-11-19 18:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0004_alter_empresa_classificacao'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('avaliacao', '0004_remove_formulario_classificacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario',
            name='Empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.empresa'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='Usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
