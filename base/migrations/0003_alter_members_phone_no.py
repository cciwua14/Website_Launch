# Generated by Django 4.1 on 2022-08-28 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_members_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='phone_no',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
