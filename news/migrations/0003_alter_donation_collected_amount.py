# Generated by Django 4.0.4 on 2022-05-25 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_donation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='collected_amount',
            field=models.IntegerField(),
        ),
    ]