# Generated by Django 3.2.6 on 2022-04-05 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0003_alter_mentor_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]