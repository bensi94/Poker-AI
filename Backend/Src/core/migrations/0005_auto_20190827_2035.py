# Generated by Django 2.2.2 on 2019-08-27 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190823_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='average_pot',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='table',
            name='hand_count',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='table',
            name='max_players',
            field=models.PositiveSmallIntegerField(default=9),
        ),
        migrations.AlterField(
            model_name='table',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('W', 'Waiting'), ('C', 'Closed')], default='W', max_length=1),
        ),
        migrations.AlterField(
            model_name='table',
            name='type',
            field=models.CharField(choices=[('C', 'Cash'), ('T', 'Tournament')], default='C', max_length=1),
        ),
    ]
