# Generated by Django 4.0.4 on 2022-05-14 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0002_product_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='model',
            field=models.CharField(default='v.sol 233', max_length=245),
            preserve_default=False,
        ),
    ]
