# Generated by Django 3.1.2 on 2020-10-10 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_auto_20201010_1347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auction',
            old_name='pulbication_date',
            new_name='publication_date',
        ),
    ]
