# Generated by Django 4.0.3 on 2022-05-04 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ElectronicBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('mail', models.CharField(max_length=255, unique=True)),
                ('phone', models.CharField(max_length=255, unique=True)),
                ('origin', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Kind',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Electronic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('publishYear', models.IntegerField()),
                ('code', models.CharField(max_length=255, unique=True)),
                ('ImportPrice', models.FloatField()),
                ('ElectronicBrandID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronic.electronicbrand')),
                ('kindID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='electronic.kind')),
            ],
        ),
    ]
