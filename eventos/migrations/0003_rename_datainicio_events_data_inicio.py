# Generated by Django 4.2 on 2023-04-16 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_events_creator'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='dataInicio',
            new_name='data_inicio',
        ),
    ]
