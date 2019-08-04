from django.db.models import  Q,F
from django.shortcuts import render
from rest_framework.views import  APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
# Create your views here.
from home import serializer
from home import  models
from Myproject.utils import  my_filter


def filtert_chace(queryset,request):
    is_jinritehui = True if request.GET.get("jinritehui") == "1" else False
    if is_jinritehui:
        value_id_list = request.conn.get("jinritehui").decode()
        value_id_list=eval(value_id_list)
        queryset=queryset.filter(id__in=value_id_list)

        return queryset
    else :
        return queryset



class Area(ListAPIView):
    queryset = models.Area.objects.filter(is_show=True)
    serializer_class =serializer.AreaSerializer

class Area_house(ListAPIView):
    queryset = models.Housing.objects.filter(is_dele=0, is_show=1)
    serializer_class = serializer.hourseSerializer
    pagination_class = my_filter.CoursePageNumberPagination
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(xiaoqu__xiaozheng__area__name=request.GET.get("area"))
        queryset = filtert_chace(queryset,request)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class Ditie_house(ListAPIView):
    queryset = models.Housing.objects.filter(is_dele=0, is_show=1)
    serializer_class = serializer.hourseSerializer
    pagination_class = my_filter.CoursePageNumberPagination
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(xiaoqu__ditie__id=request.GET.get("ditie"))
        queryset = filtert_chace(queryset, request)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class Jiage_house(ListAPIView):
    queryset = models.Housing.objects.filter(is_dele=0, is_show=1)
    serializer_class = serializer.hourseSerializer
    pagination_class = my_filter.CoursePageNumberPagination
    def list(self, request, *args, **kwargs):
        jiage=request.GET.get("jiage")
        queryset = self.filter_queryset(self.get_queryset())
        if jiage=="9999":
            queryset = queryset.filter(Q(xianjia__gt=3000))
        elif jiage=="3000":
            print("走了着")
            queryset = queryset.filter(Q(xianjia__gt=2000)&Q(xianjia__lt=3000))
            print("qerty是",queryset)
            print("价格是",queryset.first().xianjia)
        elif jiage=="2000":
            queryset = queryset.filter(Q(xianjia__gt=1500) & Q(xianjia__lt=2000))
        elif jiage=="1500":
            queryset = queryset.filter(Q(xianjia__gt=1000) & Q(xianjia__lt=1500))
        elif jiage=="1000":
                    queryset = queryset.filter(Q(xianjia__gt=700) & Q(xianjia__lt=1000))
        elif jiage == "700":
            queryset = queryset.filter(Q(xianjia__gt=500) & Q(xianjia__lt=700))
        else :
            queryset = queryset.filter(Q(xianjia__lt=500))
        queryset = filtert_chace(queryset,request)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
class Huxing(ListAPIView):
    queryset = models.Housing.objects.filter(is_dele=0, is_show=1)
    serializer_class = serializer.hourseSerializer
    pagination_class = my_filter.CoursePageNumberPagination
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        type_id=request.GET.get("type_id")
        queryset = queryset.filter(expenses=type_id)
        queryset = filtert_chace(queryset, request)
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

