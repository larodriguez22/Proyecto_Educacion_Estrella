# Generated by Django 3.2.6 on 2022-04-06 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_vocacional', '0005_auto_20220406_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preguntasrespondidas',
            name='testUsuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intentos', to='test_vocacional.testusuario'),
        ),
    ]