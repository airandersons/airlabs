# Generated by Django 5.1.6 on 2025-02-21 04:47

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0006_alter_post_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
