# Generated by Django 4.0.5 on 2022-07-19 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChannelNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resourceId', models.CharField(max_length=64)),
                ('channelId', models.CharField(max_length=64)),
                ('expiration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(null=True, verbose_name='Order number')),
                ('delivery_time', models.DateField(null=True, verbose_name='Order delivery time')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=8, null=True, verbose_name='Order cost, $')),
                ('cost_R', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Order cost, ₽')),
            ],
        ),
    ]