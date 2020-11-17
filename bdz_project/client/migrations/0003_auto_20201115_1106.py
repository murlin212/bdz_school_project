# Generated by Django 2.2.12 on 2020-11-15 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_auto_20201102_2101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_type', models.CharField(max_length=20)),
                ('discount', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='route',
            name='end_station',
        ),
        migrations.RemoveField(
            model_name='route',
            name='starting_station',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='departure_date',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='route',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='train_id',
        ),
        migrations.AddField(
            model_name='route',
            name='arrival_date',
            field=models.DateTimeField(default=None, verbose_name='arrival date'),
        ),
        migrations.AddField(
            model_name='route',
            name='departure_date',
            field=models.DateTimeField(default=None, verbose_name='departure date'),
        ),
        migrations.AddField(
            model_name='route',
            name='duration',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='route',
            name='train_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ticket',
            name='ticket_type',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='route',
            name='end_station_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='end_station_id', to='client.Station'),
        ),
        migrations.AddField(
            model_name='route',
            name='starting_station_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='starting_station_id', to='client.Station'),
        ),
    ]