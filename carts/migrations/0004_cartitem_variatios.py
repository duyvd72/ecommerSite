# Generated by Django 4.0.4 on 2022-05-04 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_variation'),
        ('carts', '0003_remove_cartitem_sell_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='variatios',
            field=models.ManyToManyField(blank=True, to='store.variation'),
        ),
    ]
