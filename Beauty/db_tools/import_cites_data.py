# -*- coding: utf-8 -*-
__author__ = 'panchao'

import sys
import os

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Beauty.settings')

import django

django.setup()

from cites.models import Cites, CitesCategory, HotCites

from db_tools.data.cites_data import cites_data


def set_cites_type():
    # 设置城市类型表
    for item in cites_data["alphabet"]:
        type_instance = CitesCategory()
        type_instance.city_name = item
        type_instance.type_name = item
        type_instance.save()


def set_cites_list():
    # 设置城市列表
    data = cites_data["cityList"]
    for item in data:
        for sub_cites in item["cities"]:
            cites_instance = Cites()
            cites_instance.city_type = item["idx"]
            cites_instance.city_name = sub_cites["name"]
            cites_instance.city_en_name = sub_cites["pinyin"]
            cites_instance.latitude = sub_cites["latitude"]
            cites_instance.longitude = sub_cites["longitude"]
            cites_instance.save()


def set_hot_cites():
    # 设置热门城市列表
    data = cites_data["hotList"]
    for item in data:
        hot_instance = HotCites()
        hot_instance.city_type = item["idx"]
        hot_instance.city_name = "热门城市"
        hot_instance.city_en_name = "remenchengshi"
        hot_instance.latitude = item["latitude"]
        hot_instance.longitude = item["longitude"]
        hot_instance.save()


set_cites_type()
set_cites_list()
set_hot_cites()