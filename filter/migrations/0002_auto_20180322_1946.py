# Generated by Django 2.0.2 on 2018-03-22 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modell',
            name='status',
            field=models.CharField(max_length=100),
        ),
    ]
