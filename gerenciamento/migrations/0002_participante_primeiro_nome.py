# Generated by Django 3.2.14 on 2022-11-06 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participante',
            name='primeiro_nome',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
