# Generated by Django 4.2 on 2023-04-16 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0004_rename_datatermino_events_data_termino'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='carga',
            new_name='carga_horaria',
        ),
    ]