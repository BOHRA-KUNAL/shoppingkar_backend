# Generated by Django 4.1.2 on 2022-10-27 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_promotions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Promotions',
            field=models.ManyToManyField(null=True, to='store.promotion'),
        ),
    ]