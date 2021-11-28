# Generated by Django 3.2.9 on 2021-11-26 01:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import hashid_field.field


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UNMeetUser',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('link', hashid_field.field.HashidAutoField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', min_length=10, prefix='UNMEET', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=400, null=True)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('date_start', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_end', models.DateTimeField()),
                ('attendants', models.ManyToManyField(related_name='attendants_meeting', to='meetings.UNMeetUser')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host_meeting', to='meetings.unmeetuser')),
            ],
        ),
    ]