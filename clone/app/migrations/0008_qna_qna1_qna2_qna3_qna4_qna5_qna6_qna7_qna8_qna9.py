# Generated by Django 3.1.5 on 2021-05-26 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210507_1559'),
    ]

    operations = [
        migrations.CreateModel(
            name='QNA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='QNA1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='QNA2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='QNA3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='QNA4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='QNA5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='QNA6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='QNA7',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='QNA8',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='QNA9',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(max_length=100)),
            ],
        ),
    ]
