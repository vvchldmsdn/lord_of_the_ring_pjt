# Generated by Django 3.2.7 on 2022-11-22 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=6)),
                ('description', models.TextField()),
                ('age', models.IntegerField(default=0)),
                ('image', models.TextField()),
                ('race', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('participant', models.ManyToManyField(related_name='incident_character', to='features.Character')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('location_lat', models.FloatField()),
                ('location_lng', models.FloatField()),
                ('description', models.TextField()),
                ('image', models.TextField()),
                ('happen', models.ManyToManyField(related_name='region_incident', to='features.Incident')),
                ('passed', models.ManyToManyField(related_name='region_character', to='features.Character')),
            ],
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('under', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='family_under', to='features.character')),
                ('upper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='family_upper', to='features.character')),
            ],
        ),
    ]
