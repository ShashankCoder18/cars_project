# Generated by Django 2.1 on 2020-05-24 17:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
        ('offices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('seats', models.IntegerField()),
                ('colour', models.CharField(max_length=200)),
                ('colour1', models.CharField(blank=True, max_length=200)),
                ('colour2', models.CharField(blank=True, max_length=200)),
                ('rating', models.IntegerField()),
                ('photo_main', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('is_available', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='companies.Company')),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='offices.Office')),
            ],
        ),
    ]
