# Generated by Django 5.1.4 on 2024-12-11 21:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название организации')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('members', models.ManyToManyField(related_name='organizations', to=settings.AUTH_USER_MODEL, verbose_name='Участники')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_organizations', to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_task', models.SmallIntegerField(choices=[(0, 'Новая'), (1, 'В работе'), (2, 'На проверке'), (3, 'Выполнено')], default=0, verbose_name='Статус задачи')),
                ('title', models.CharField(max_length=255, verbose_name='Название задачи')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание задачи')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='tasks_board.organization', verbose_name='Организация')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель')),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationMembership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joined_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата вступления')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks_board.organization')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('organization', 'user')},
            },
        ),
    ]