# Generated by Django 5.1.1 on 2024-11-03 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AIUApp', '0003_room_host'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['updated', 'created']},
        ),
    ]
