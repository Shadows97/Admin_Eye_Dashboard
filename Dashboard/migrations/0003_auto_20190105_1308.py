# Generated by Django 2.1.4 on 2019-01-05 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0002_auto_20190105_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disk_info',
            name='size_free',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='disk_info',
            name='size_used',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='disk_info',
            name='total_size',
            field=models.BigIntegerField(),
        ),
    ]