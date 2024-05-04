# Generated by Django 4.1.13 on 2024-05-04 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SessionData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SessionEndedAt', models.CharField(blank=True, max_length=12, null=True)),
                ('SessionStartedAt', models.CharField(blank=True, max_length=12, null=True)),
                ('arousal', models.IntegerField()),
                ('attention', models.IntegerField()),
                ('dominantEmotion', models.CharField(max_length=50)),
                ('feature_1', models.CharField(max_length=50)),
                ('feature_2', models.CharField(max_length=50)),
                ('feature_3', models.CharField(max_length=50)),
                ('feature_4', models.CharField(max_length=50)),
                ('feature_5', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('userEmail', models.CharField(max_length=100)),
                ('valence', models.FloatField()),
                ('volume', models.FloatField()),
            ],
        ),
    ]
