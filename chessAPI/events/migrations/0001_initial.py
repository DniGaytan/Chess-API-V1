# Generated by Django 3.1.1 on 2023-12-27 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=1200)),
                ('picture_url', models.URLField()),
                ('is_active', models.BooleanField()),
                ('event_type', models.CharField(choices=[('league', 'League'), ('tournament', 'Tournament'), ('friendly', 'Friendly')], default='league', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EventPlayers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_score', models.IntegerField()),
                ('total_wins', models.IntegerField()),
                ('total_loses', models.IntegerField()),
                ('total_tites', models.IntegerField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='events.event')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='players.player')),
            ],
        ),
    ]