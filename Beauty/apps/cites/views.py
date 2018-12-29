from django.shortcuts import render
from rest_framework import mixins, filters, viewsets
from rest_framework.response import Response
from .models import Cites
from .serializers import CitesSerializers

from .static_data import cites_type
from extra_apps.common.common_data import SUCCESS

# Create your views here.


class CitesListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Cites.objects.all()
    serializer_class = CitesSerializers

    def list(self, request, *args, **kwargs):
        """
        重写 mixins.ListModelMixin中的list方法
        :return:
        """
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        query_data = serializer.data
        list1 = []
        all_list = []
        new_data = {}
        for type_item in cites_type:
            print(type_item)
            for data_item in query_data:
                if data_item['city_type'] == type_item:
                    new_data['city_type'] = type_item
                    new_data['type_name'] = type_item
                    list1.append(data_item)
            if len(list1):
                new_data['cites'] = list1
                all_list.append(new_data)
                list1 = []
                new_data = {}
        d = {"data": all_list}
        data = {}
        data.update(SUCCESS)
        data.update(d)
        return Response(data)