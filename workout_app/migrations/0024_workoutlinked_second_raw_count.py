# Generated by Django 3.1.7 on 2021-03-24 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout_app', '0023_auto_20210323_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='workoutlinked',
            name='second_raw_count',
            field=models.IntegerField(default=0),
        ),
    ]
