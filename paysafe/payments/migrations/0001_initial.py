# Generated by Django 3.1.7 on 2021-02-22 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('merchantCustomerId', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('id', models.CharField(max_length=64)),
                ('paymentToken', models.CharField(max_length=64)),
            ],
        ),
    ]