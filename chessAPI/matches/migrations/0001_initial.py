# Generated by Django 3.1.1 on 2023-12-27 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0003_auto_20231227_1034'),
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('result', models.CharField(choices=[('upcoming', 'Upcoming'), ('whites', 'Whites'), ('blacks', 'Blacks'), ('draw', 'Draw')], default='upcoming', max_length=100)),
                ('blacks_player', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='blacks_player', to='players.player')),
                ('event', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='events.event')),
                ('whites_player', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='whites_player', to='players.player')),
            ],
        ),
    ]