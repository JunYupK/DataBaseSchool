# Generated by Django 4.0.3 on 2022-04-15 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_quiz'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addclass',
            old_name='profname',
            new_name='profid',
        ),
    ]
