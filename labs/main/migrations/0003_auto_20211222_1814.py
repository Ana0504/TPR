# Generated by Django 3.2.2 on 2021-12-22 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20211221_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tprlab6stockdata',
            name='stockClose',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='tprlab6stockdata',
            name='stockHigh',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='tprlab6stockdata',
            name='stockLow',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='tprlab6stockdata',
            name='stockOpen',
            field=models.PositiveIntegerField(),
        ),
    ]
