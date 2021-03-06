# Generated by Django 4.0.4 on 2022-05-02 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_mobilephoneitem_internal_memory'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_name',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
    ]
