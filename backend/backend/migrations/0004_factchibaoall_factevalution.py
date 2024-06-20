# Generated by Django 3.2.25 on 2024-06-15 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_rename_donvigiatringuong_nguongcanhbao_dieukientheodoi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factchibaoall',
            fields=[
                ('MaChiBao', models.AutoField(primary_key=True, serialize=False)),
                ('MaChungKhoan', models.CharField(max_length=255)),
                ('NgayGiaoDich', models.DateTimeField()),
                ('TenChiBao', models.CharField(max_length=10)),
                ('GiaTriChiBao', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Factevalution',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('MaChungKhoan', models.CharField(max_length=255)),
                ('NgayGiaoDich', models.DateTimeField()),
                ('PE', models.FloatField()),
                ('PB', models.FloatField()),
                ('NganhCongNghiepPE', models.FloatField()),
                ('NganhCongNghiepPB', models.FloatField()),
                ('PEChungKhoan', models.FloatField()),
                ('PBChungKhoan', models.FloatField()),
            ],
        ),
    ]
