from datetime import datetime
from django.db import models

# Create your models here.


class CitesCategory(models.Model):

    city_type = models.CharField(default="", max_length=20, verbose_name="地域类别", help_text="地域类别")
    type_name = models.CharField(default="", max_length=20, verbose_name="城市类别", help_text="城市类别")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "城市类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.type_name


class Cites(models.Model):
    city_type = models.CharField(default="", max_length=20, verbose_name="地域类别", help_text="地域类别")
    city_name = models.CharField(default="", max_length=20, verbose_name="城市名", help_text="城市名")
    city_en_name = models.CharField(default="", max_length=200, verbose_name="城市名拼音", help_text="城市名拼音")
    latitude = models.FloatField(null=True, blank=True, verbose_name="纬度", help_text="纬度")
    longitude = models.FloatField(null=True, blank=True, verbose_name="经度", help_text="经度")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "城市列表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.city_name


class HotCites(models.Model):
    city_type = models.CharField(default="", max_length=20, verbose_name="地域类别", help_text="地域类别")
    city_name = models.CharField(default="", max_length=20, verbose_name="城市名", help_text="城市名")
    city_en_name = models.CharField(default="", max_length=200, verbose_name="城市名拼音", help_text="城市名拼音")
    latitude = models.FloatField(null=True, blank=True, verbose_name="纬度", help_text="纬度")
    longitude = models.FloatField(null=True, blank=True, verbose_name="经度", help_text="经度")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "热门城市列表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.city_name
