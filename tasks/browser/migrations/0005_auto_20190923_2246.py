# Generated by Django 2.2.5 on 2019-09-23 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0004_auto_20190923_2147'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name_plural': 'tasks'},
        ),
        migrations.AlterField(
            model_name='task',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='children', to='browser.Task'),
        ),
        migrations.AlterUniqueTogether(
            name='task',
            unique_together={('name', 'parent')},
        ),
    ]