# Generated by Django 2.0.1 on 2018-02-15 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogManagement', '0005_auto_20180214_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='validFor_endDateTime',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='validFor_startDateTime',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
