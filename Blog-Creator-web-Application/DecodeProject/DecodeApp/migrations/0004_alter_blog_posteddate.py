# Generated by Django 4.1.3 on 2023-04-20 10:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DecodeApp', '0003_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='postedDate',
            field=models.DateField(default=datetime.date(2023, 4, 20)),
        ),
    ]
