# Generated by Django 5.0.1 on 2024-02-26 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.BigIntegerField(default=0),
        ),
    ]
