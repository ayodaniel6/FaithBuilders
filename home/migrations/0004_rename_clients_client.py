# Generated by Django 4.2.1 on 2023-05-19 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_clients_phone'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Clients',
            new_name='Client',
        ),
    ]
