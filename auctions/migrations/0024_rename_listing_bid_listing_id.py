# Generated by Django 4.2 on 2023-05-18 01:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0023_alter_bid_bid_alter_bid_listing_alter_bid_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='listing',
            new_name='listing_id',
        ),
    ]
