# Generated by Django 5.0.7 on 2024-07-25 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otp',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='otp',
            name='otp',
        ),
        migrations.AddField(
            model_name='otp',
            name='otp_hash',
            field=models.CharField(default='default_hash_value', max_length=64),
        ),
    ]
