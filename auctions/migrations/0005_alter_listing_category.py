# Generated by Django 4.2 on 2023-05-12 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_rename_categories_categorie_rename_listings_listing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.categorie'),
        ),
    ]
