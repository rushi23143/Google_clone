# Generated by Django 3.1.5 on 2021-05-26 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20210526_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='QNA1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(max_length=100)),
            ],
        ),
    ]
