# Generated by Django 5.1.4 on 2025-01-12 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='status_task',
            field=models.SmallIntegerField(choices=[(0, 'New'), (1, 'In work'), (2, 'Review'), (3, 'Completed')], default=0, verbose_name='Статус задачи'),
        ),
    ]