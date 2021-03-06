# Generated by Django 3.2.6 on 2021-08-30 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector_reporte', models.CharField(choices=[('SUR', 'SUR'), ('CENTRO', 'CENTRO'), ('NORTE', 'NORTE')], max_length=40)),
                ('direccion_reporte', models.CharField(max_length=120)),
                ('categoria_reporte', models.CharField(choices=[('DANOS_EN_LA_VIA_PUBLICA', 'DAÑOS EN LA VIA PUBLICA'), ('DANOS_EN_ESPACIOS_PUBLICOS', 'DAÑOS EN ESPACIOS PÚBLICOS'), ('ANIMALES_ABANDONADOS_EN_LA_VIA_PUBLICA', 'ANIMALES ABANDONADOS EN LA VÍA PÚBLICA'), ('BASURA_EN_LUGARES_INCORRECTOS', 'BASURA EN LUGARES INCORRECTOS')], max_length=120)),
                ('evidencia_reporte', models.FileField(upload_to='uploads/%Y/%m/%d/')),
                ('descripcion_reporte', models.CharField(max_length=240)),
                ('usuario_reporte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
