# Generated by Django 2.0.2 on 2018-03-25 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0010_auto_20180325_2151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermentions',
            old_name='userm',
            new_name='tweet',
        ),
        migrations.AlterField(
            model_name='hashtags',
            name='tweetidd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filter.Modell'),
        ),
        migrations.AlterField(
            model_name='usermentions',
            name='tweet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filter.Modell'),
        ),
    ]
