# Generated by Django 4.0.5 on 2022-07-20 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordersOnlineUpdates', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='delivery_time',
            new_name='time',
        ),
    ]
