# Generated by Django 2.2.dev20180801155202 on 2018-08-02 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trafficlight',
            name='status',
        ),
        migrations.AddField(
            model_name='trafficlight',
            name='area',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='trafficlight',
            name='latitude',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='trafficlight',
            name='logitude',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='trafficlight',
            name='persons',
            field=models.IntegerField(default=0),
        ),
    ]
