# Generated by Django 4.0.3 on 2022-04-23 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_regclass_date_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='data',
            field=models.DateTimeField(null=True),
        ),
    ]
