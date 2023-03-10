# Generated by Django 3.2.6 on 2023-02-24 04:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_userdetails_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetails',
            old_name='status',
            new_name='is_active',
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
