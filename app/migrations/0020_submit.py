# Generated by Django 4.0.4 on 2022-05-09 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0019_remove_score_score_score_is_pass'),
    ]

    operations = [
        migrations.CreateModel(
            name='submit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_pass', models.BooleanField(default=False)),
                ('classid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.class')),
                ('problemid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.problem')),
                ('quizid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.quiz')),
                ('studentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
