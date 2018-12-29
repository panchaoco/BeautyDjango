# -*- coding: utf-8 -*-
__author__ = 'panchao'

from rest_framework import serializers

from cites.models import Cites


class CitesSerializers(serializers.ModelSerializer):
    """
    城市列表的序列化
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Cites
        fields = "__all__"