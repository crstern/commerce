# Generated by Django 3.1.2 on 2020-10-18 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_auto_20201018_1618'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auction',
            old_name='isSold',
            new_name='is_sold',
        ),
    ]