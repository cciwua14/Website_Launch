# Generated by Django 4.1 on 2022-08-28 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='phone_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]