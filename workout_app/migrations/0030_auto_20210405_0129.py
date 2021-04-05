# Generated by Django 3.1.7 on 2021-04-05 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout_app', '0029_auto_20210404_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='workoutlinked',
            name='duration',
            field=models.DurationField(null=True),
        ),
        migrations.AddField(
            model_name='workouttype',
            name='has_duration',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
