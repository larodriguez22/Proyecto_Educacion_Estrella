# Generated by Django 3.2.6 on 2022-04-05 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_vocacional', '0002_auto_20220405_1008'),
        ('pregunta', '0006_preguntasrespondidas_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preguntasrespondidas',
            name='pregunta',
        ),
        migrations.RemoveField(
            model_name='preguntasrespondidas',
            name='respuesta',
        ),
        migrations.RemoveField(
            model_name='preguntasrespondidas',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='ElegirRespuesta',
        ),
        migrations.DeleteModel(
            name='Pregunta',
        ),
        migrations.DeleteModel(
            name='PreguntasRespondidas',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]