# Generated by Django 4.1.1 on 2022-10-28 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_remove_imagemodel_mainimage_remove_imagemodel_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.DeleteModel(
            name='ImageModel',
        ),
    ]
