# Generated by Django 3.2.6 on 2022-04-02 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0003_reserva_estudiante'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='estudiante',
        ),
        migrations.AddField(
            model_name='reserva',
            name='estu',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
