from django.contrib.auth.models import AbstractUser
from django.db import models
from . import settings

class Dimmachungkhoan(models.Model):
    MaChungKhoan = models.CharField(max_length=20)
    TenCongTy = models.CharField(max_length=255)
    TenNganh = models.CharField(max_length=255)

class Account(AbstractUser):
    MaTaiKhoan = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    HoVaTen = models.CharField(max_length=255)
    
class Nguongcanhbao(models.Model):
    MaCanhBao = models.AutoField(primary_key=True)
    MaTaiKhoan = models.ForeignKey(
        Account,  on_delete=models.CASCADE
    )
    BotToken = models.CharField(max_length=255)
    ChatID = models.CharField(max_length=255)
    MaChungKhoan = models.CharField(max_length=255)
    LoaiChiBao = models.CharField(max_length=255)
    GiaTriNguong = models.FloatField()
    DieuKienTheoDoi = models.CharField(max_length=10)

class Factlichsugia(models.Model):
    MaLichSuGia = models.AutoField(primary_key=True)
    MaChungKhoan = models.CharField(max_length=255)
    NgayGiaoDich = models.DateTimeField(auto_now_add=False)
    GiaMo = models.FloatField()
    GiaDong = models.FloatField()
    GiaCaoNhat = models.FloatField()
    GiaThapNhat = models.FloatField()
    KhoiLuong = models.IntegerField()

class Factchibao(models.Model):
    MaChiBao = models.AutoField(primary_key=True)
    MaChungKhoan = models.CharField(max_length=255)
    NgayGiaoDich = models.DateTimeField(auto_now_add=False)
    TenChiBao = models.CharField(max_length=10)
    GiaTriChiBao = models.FloatField()

class Factchibaoall(models.Model):
    MaChiBao = models.AutoField(primary_key=True)
    MaChungKhoan = models.CharField(max_length=255)
    NgayGiaoDich = models.DateTimeField(auto_now_add=False)
    TenChiBao = models.CharField(max_length=10)
    GiaTriChiBao = models.FloatField()


class Factevalution(models.Model):
    id = models.AutoField(primary_key=True)
    MaChungKhoan = models.CharField(max_length=255)
    NgayGiaoDich = models.DateTimeField(auto_now_add=False)
    PE = models.FloatField()
    PB = models.FloatField()
    NganhCongNghiepPE = models.FloatField()
    NganhCongNghiepPB = models.FloatField()
    PEChungKhoan = models.FloatField()
    PBChungKhoan = models.FloatField()