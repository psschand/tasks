# Generated by Django 2.1 on 2019-09-29 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0013_auto_20190929_0353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='end_date',
            field=models.DateTimeField(blank=True, verbose_name='End date'),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateTimeField(blank=True, verbose_name='Start date'),
        ),
    ]
