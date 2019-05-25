
# Generated by Django 2.2.1 on 2019-05-25 09:05
#fe3183993ab932b6d106d50d75ff8bbc7eb3233f

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deserts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=20)),
                ('price', models.DecimalField(decimal_places=3, default=0.0, max_digits=50)),
                ('mass', models.IntegerField(default=0.0)),
                ('photo', models.ImageField(upload_to='deserts_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Drinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=20)),
                ('description', models.TextField(max_length=500)),
                ('price', models.DecimalField(decimal_places=3, default=0.0, max_digits=50)),
                ('ml', models.IntegerField(default=0.0)),
                ('photo', models.ImageField(upload_to='drinks_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Pizzas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=20)),
                ('description', models.TextField(max_length=500)),
                ('price', models.DecimalField(decimal_places=3, default=0.0, max_digits=50)),
                ('mass', models.IntegerField(default=0.0)),
                ('photo', models.ImageField(upload_to='pizza_images/')),
            ],
        ),
    ]
