# Generated by Django 4.0.4 on 2022-06-04 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_news_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='projects',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
