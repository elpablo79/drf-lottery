# Generated by Django 4.0.4 on 2022-04-27 14:38

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('start', models.DateField()),
                ('end', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=50)),
                ('perday', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WinPerDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(verbose_name=datetime.datetime(2022, 4, 27, 16, 38, 27, 259225))),
                ('winnings', models.IntegerField(default=0)),
                ('attempts', models.IntegerField(default=0)),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.contest')),
            ],
        ),
        migrations.CreateModel(
            name='UserWinningsPerDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(auto_now_add=True)),
                ('winnings', models.IntegerField(default=1)),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.contest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserToContest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.contest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='contest',
            name='prize',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.prize'),
        ),
        migrations.AddConstraint(
            model_name='userwinningsperday',
            constraint=models.UniqueConstraint(fields=('user', 'contest', 'day'), name='unique_user_contest_date'),
        ),
    ]