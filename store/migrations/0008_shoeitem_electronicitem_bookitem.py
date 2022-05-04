# Generated by Django 4.0.3 on 2022-05-04 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('electronic', '0001_initial'),
        ('shoes', '0001_initial'),
        ('book', '0001_initial'),
        ('store', '0007_variation'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoeItem',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='store.item')),
                ('size', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('shoeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoes.shoes')),
            ],
            bases=('store.item',),
        ),
        migrations.CreateModel(
            name='ElectronicItem',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='store.item')),
                ('color', models.CharField(max_length=255)),
                ('warranty', models.CharField(max_length=255)),
                ('ElectronicID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronic.electronic')),
            ],
            bases=('store.item',),
        ),
        migrations.CreateModel(
            name='BookItem',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='store.item')),
                ('edition', models.CharField(max_length=255)),
                ('bookID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book')),
            ],
            bases=('store.item',),
        ),
    ]
