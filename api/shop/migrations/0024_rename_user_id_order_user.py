# Generated by Django 4.1.1 on 2022-12-02 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_alter_order_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user_id',
            new_name='user',
        ),
    ]
