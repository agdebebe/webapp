# Generated by Django 2.2 on 2019-12-25 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20191211_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderitems',
            field=models.ManyToManyField(to='cart.Cart'),
        ),
    ]
