# Generated by Django 4.1.5 on 2023-01-26 16:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
