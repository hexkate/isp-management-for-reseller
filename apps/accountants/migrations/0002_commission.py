# Generated by Django 4.0.4 on 2022-06-25 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commission', models.DecimalField(decimal_places=2, default=20, max_digits=2)),
            ],
        ),
    ]