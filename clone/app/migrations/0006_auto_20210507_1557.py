# Generated by Django 3.1.5 on 2021-05-07 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_website_xss'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='xss',
            field=models.CharField(max_length=100),
        ),
    ]
