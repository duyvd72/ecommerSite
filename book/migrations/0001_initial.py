# Generated by Django 4.0.3 on 2022-05-04 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=255)),
                ('yearOfBirth', models.CharField(max_length=255)),
                ('homeTown', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('isbnCode', models.CharField(max_length=255)),
                ('publishYear', models.CharField(max_length=255)),
                ('pageNum', models.IntegerField()),
                ('importPrice', models.FloatField()),
            ],
            options={
                'verbose_name': 'Books',
                'verbose_name_plural': 'Books',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Book_Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=255)),
                ('AuthorID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.author')),
                ('BookID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='PublisherID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='book.publisher'),
        ),
    ]
