# Generated by Django 2.2.2 on 2019-08-27 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190827_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
