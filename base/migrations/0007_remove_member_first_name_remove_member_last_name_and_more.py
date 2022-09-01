# Generated by Django 4.1 on 2022-08-30 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_member_first_name_alter_member_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='member',
            name='last_name',
        ),
        migrations.AddField(
            model_name='member',
            name='name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
