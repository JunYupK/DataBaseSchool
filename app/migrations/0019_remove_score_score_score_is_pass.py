# Generated by Django 4.0.4 on 2022-05-09 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_score_problemid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='Score',
        ),
        migrations.AddField(
            model_name='score',
            name='is_pass',
            field=models.BooleanField(default=False),
        ),
    ]
