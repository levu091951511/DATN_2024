# Generated by Django 3.2.25 on 2024-06-15 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_dimmachungkhoan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nguongcanhbao',
            old_name='DonViGiaTriNguong',
            new_name='DieuKienTheoDoi',
        ),
    ]
