# Generated by Django 3.2.9 on 2021-11-20 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20211120_2325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Breed_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('information', models.CharField(max_length=100000)),
            ],
        ),
    ]
