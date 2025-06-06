# Generated by Django 4.2.20 on 2025-05-19 18:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("paginas", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="evento",
            old_name="tipoEvento",
            new_name="tipo_evento",
        ),
        migrations.RenameField(
            model_name="localizacaoevento",
            old_name="capacidadeMaxima",
            new_name="capacidade_maxima",
        ),
        migrations.RenameField(
            model_name="orcamento",
            old_name="valorPrevisto",
            new_name="valor_previsto",
        ),
        migrations.RenameField(
            model_name="orcamento",
            old_name="valorReal",
            new_name="valor_real",
        ),
        migrations.RemoveField(
            model_name="evento",
            name="dataEvento",
        ),
        migrations.AddField(
            model_name="evento",
            name="data_evento",
            field=models.DateTimeField(default="2025-01-01"),
            preserve_default=False,
        ),
    ]
