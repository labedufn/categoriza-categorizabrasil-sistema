# Generated by Django 4.2.16 on 2024-11-19 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulario',
            name='classificacao',
            field=models.CharField(default='default_value', max_length=100),
        ),
    ]
