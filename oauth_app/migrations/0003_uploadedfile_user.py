# Generated by Django 4.2.11 on 2024-03-29 22:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oauth_app', '0002_uploadedfile_comment_uploadedfile_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
