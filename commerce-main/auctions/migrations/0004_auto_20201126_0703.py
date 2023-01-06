# Generated by Django 3.1.3 on 2020-11-26 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20201126_0651'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Q', 'Quick sell'), ('F', 'Fashion'), ('T', 'Toys'), ('E', 'Electronics'), ('H', 'Home'), ('O', 'Other')], default='Q', max_length=1),
        ),
        migrations.AddField(
            model_name='listing',
            name='description',
            field=models.TextField(default='Description'),
        ),
        migrations.AddField(
            model_name='listing',
            name='imgSrc',
            field=models.URLField(blank='True'),
        ),
        migrations.AddField(
            model_name='listing',
            name='name',
            field=models.CharField(default='Name', max_length=150),
        ),
        migrations.AddField(
            model_name='listing',
            name='startBid',
            field=models.IntegerField(default=0),
        ),
    ]