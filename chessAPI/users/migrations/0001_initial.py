# Generated by Django 3.1.1 on 2023-12-27 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserExtra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthdate', models.DateField()),
                ('picture_link', models.URLField(max_length=255)),
            ],
            options={
                'db_table': 'user_extra',
            },
        ),
    ]
