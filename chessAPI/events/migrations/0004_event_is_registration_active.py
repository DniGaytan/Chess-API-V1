# Generated by Django 3.1.1 on 2023-12-27 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20231227_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_registration_active',
            field=models.BooleanField(default=True),
        ),
    ]