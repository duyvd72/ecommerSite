# Generated by Django 4.0.4 on 2022-05-04 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_cartitem_variatios'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='variatios',
            new_name='variations',
        ),
    ]
