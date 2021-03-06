# Generated by Django 3.0 on 2019-12-15 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=50)),
                ('comuna', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('correo', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ordentrabajo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ot', models.IntegerField()),
                ('fecha', models.IntegerField()),
                ('hora_inicio', models.IntegerField()),
                ('hora_termino', models.IntegerField()),
                ('id_ascensor', models.CharField(max_length=100)),
                ('modelo_ascensor', models.CharField(max_length=100)),
                ('fallas_detectadas', models.CharField(max_length=100)),
                ('reparacion_efectuada', models.CharField(max_length=100)),
                ('piezas_cambiadas', models.CharField(max_length=100)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Cliente')),
                ('tecnico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Tecnico')),
            ],
        ),
    ]
