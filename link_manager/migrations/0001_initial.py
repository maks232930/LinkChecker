# Generated by Django 4.2.6 on 2023-10-09 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('url', models.URLField(verbose_name='Ссылка')),
                ('condition_type', models.CharField(choices=[('json', 'JSON-валидный'), ('text', 'Есть определенный текст'), ('status_code', 'Статус 200')], max_length=20, verbose_name='Условие')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Текст для поиска')),
                ('is_active', models.BooleanField(default=True, verbose_name='Работает')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Ссылка',
                'verbose_name_plural': 'Ссылки',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_result', models.BooleanField(verbose_name='Результат')),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='link_manager.link')),
            ],
            options={
                'verbose_name': 'Результат',
                'verbose_name_plural': 'Результаты',
            },
        ),
    ]