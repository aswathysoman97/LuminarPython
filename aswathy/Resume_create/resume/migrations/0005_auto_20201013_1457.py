# Generated by Django 3.1 on 2020-10-13 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_auto_20201010_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create',
            name='dob',
            field=models.DateField(max_length=120),
        ),
    ]