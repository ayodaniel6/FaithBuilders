# Generated by Django 4.2.1 on 2023-05-22 16:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_article_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created',
            field=models.DateField(default=datetime.datetime(2023, 5, 22, 16, 7, 27, 976416, tzinfo=datetime.timezone.utc)),
        ),
    ]
