# Generated by Django 2.2.1 on 2019-05-25 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0010_auto_20190526_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzas',
            name='price',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=50),
        ),
    ]