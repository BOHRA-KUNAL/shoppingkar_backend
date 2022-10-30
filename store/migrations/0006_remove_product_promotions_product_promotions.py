# Generated by Django 4.1.2 on 2022-10-27 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_product_promotions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Promotions',
        ),
        migrations.AddField(
            model_name='product',
            name='promotions',
            field=models.ManyToManyField(blank=True, to='store.promotion'),
        ),
    ]
