# Generated by Django 3.1.7 on 2021-02-22 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='id',
            new_name='customerid',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='singleUsePaymentHandle',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
    ]
