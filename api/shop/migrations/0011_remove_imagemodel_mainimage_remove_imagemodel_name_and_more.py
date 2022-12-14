# Generated by Django 4.1.1 on 2022-10-28 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_remove_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagemodel',
            name='mainimage',
        ),
        migrations.RemoveField(
            model_name='imagemodel',
            name='name',
        ),
        migrations.AddField(
            model_name='imagemodel',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.product'),
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
