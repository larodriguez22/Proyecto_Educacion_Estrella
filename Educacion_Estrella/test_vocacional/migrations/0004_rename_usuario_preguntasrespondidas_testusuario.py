# Generated by Django 3.2.6 on 2022-04-06 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_vocacional', '0003_rename_usuario_testusuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preguntasrespondidas',
            old_name='usuario',
            new_name='testUsuario',
        ),
    ]
