# Generated by Django 5.1.5 on 2025-01-22 19:59

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
            name='Countdown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration_minutes', models.PositiveIntegerField()),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField()),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='counters', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
