# Generated by Django 2.0.2 on 2018-03-23 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0002_auto_20180322_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='modell',
            name='username',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='modell',
            name='status',
            field=models.CharField(max_length=400),
        ),
    ]
