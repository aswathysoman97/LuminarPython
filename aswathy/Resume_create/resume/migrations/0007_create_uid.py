# Generated by Django 3.1 on 2020-10-19 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_auto_20201013_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='create',
            name='uid',
            field=models.IntegerField(default='qwery'),
            preserve_default=False,
        ),
    ]
