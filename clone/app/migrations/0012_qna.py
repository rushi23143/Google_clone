# Generated by Django 3.1.5 on 2021-05-26 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_qna2_qna3_qna4_qna5_qna6_qna7_qna8_qna9'),
    ]

    operations = [
        migrations.CreateModel(
            name='QNA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=100)),
            ],
        ),
    ]