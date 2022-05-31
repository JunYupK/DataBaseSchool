# Generated by Django 4.0.4 on 2022-05-03 02:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0016_alter_class_classname'),
    ]

    operations = [
        migrations.CreateModel(
            name='problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.CharField(max_length=1000)),
                ('sql', models.CharField(max_length=100)),
                ('classid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.class')),
                ('profid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('quizid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.quiz')),
            ],
        ),
    ]
