# Generated by Django 2.2.2 on 2019-07-05 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klazor', '0004_auto_20190705_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursepart',
            name='level',
            field=models.SmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='coursepart',
            name='sequence',
            field=models.SmallIntegerField(default=1),
        ),
    ]