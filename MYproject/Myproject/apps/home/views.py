from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from home import serializer
from home import  models
from rest_framework.views import  APIView
from rest_framework.generics import ListAPIView
class Nav(ListAPIView):
    queryset = models.Nav_title.objects.filter(rank=0,is_show=True)
    serializer_class =serializer.NavSerializer
class Benner(ListAPIView):
    queryset = models.Banner.objects.filter(is_show=True)
    serializer_class =serializer.BennerSerializer

class Area(ListAPIView):
    queryset = models.Area.objects.filter(is_show=True)
    serializer_class =serializer.AreaSerializer

class Nav_Bottom(ListAPIView):
    queryset = models.Nav_title.objects.filter(rank=2, is_show=True)
    serializer_class = serializer.NavSerializer
# from django.views.decorators.cache import cache
class Housing_estate(ListAPIView):
    queryset = models.Housing_estate.objects.filter(is_show=True)
    serializer_class =serializer.Housing_estateSerializer
    def list(self,request,*args,**kwargs):
        return super(ListAPIView,self).list(self,request,*args,**kwargs)
class Room_type(ListAPIView):
    queryset = models.Room_type.objects.filter(is_show=True)
    serializer_class = serializer.Room_typeSerializer

class  JPFY(APIView):
    def get(self,request,*args,**kwargs):
        filter_func=request.GET.get("type")


        value_id_list=request.conn.get(filter_func).decode()
        value_id_list=eval(value_id_list)
        hourse_list=models.Housing.objects.filter(id__in=value_id_list)

        # print(hourse_list[0].housing_img.all().first())

        jpfser=serializer.hourseSerializer(instance=hourse_list,many=True)

        return Response(jpfser.data)
        # except Exception as f :
        #     print(f)
        #     return Response([])
from django_filters import compat, utils
from django_filters.rest_framework import filters, filterset
from django_filters.rest_framework import DjangoFilterBackend

class xxx(DjangoFilterBackend):
    filterset_base = filterset.FilterSet
    raise_exception = True
    def get_filterset_class(self, view, queryset=None):

        """
        Return the `FilterSet` class used to filter the queryset.
        """

        filterset_class = getattr(view, 'filterset_class', None)
        filterset_fields = getattr(view, 'filterset_fields', None)

        # TODO: remove assertion in 2.1
        if filterset_class is None and hasattr(view, 'filter_class'):
            utils.deprecate(
                "`%s.filter_class` attribute should be renamed `filterset_class`."
                % view.__class__.__name__)
            filterset_class = getattr(view, 'filter_class', None)

        # TODO: remove assertion in 2.1
        if filterset_fields is None and hasattr(view, 'filter_fields'):
            utils.deprecate(
                "`%s.filter_fields` attribute should be renamed `filterset_fields`."
                % view.__class__.__name__)
            filterset_fields = getattr(view, 'filter_fields', None)

        if filterset_class:
            filterset_model = filterset_class._meta.model

            # FilterSets do not need to specify a Meta class
            if filterset_model and queryset is not None:
                assert issubclass(queryset.model, filterset_model), \
                    'FilterSet model %s does not match queryset model %s' % \
                    (filterset_model, queryset.model)

            return filterset_class

        if filterset_fields and queryset is not None:
            MetaBase = getattr(self.filterset_base, 'Meta', object)
            class AutoFilterSet(self.filterset_base):
                class Meta(MetaBase):
                    print(queryset.model,filterset_fields)
                    model = queryset.model
                    fields = filterset_fields

            return AutoFilterSet

        return None
from django.db.models import  Max,Min
from home import serializer



class Area_houre(ListAPIView):
    queryset = models.Housing.objects.filter(is_dele=0,is_show=1)
    serializer_class = serializer.hourseSerializer
    def list(self,request,*args,**kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset=queryset.filter(xiaoqu__xiaozheng__area__name=request.GET.get("area"))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        print(queryset)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# def test(request):
#     print(request.conn)
#     print(request.conn.get("jrth"))
#
#
#
# # class Jrtj_list(ListAPIView):
# #     queryset =
#
#
# # from django.shortcuts import  HttpResponse
# # import datetime
# # def get_python(request):
# #     import time
# #     return HttpResponse(datetime.datetime.now())
#
#
class Today_preferential(ListAPIView):
    def get(self,request,*args,**kwargs):
        '''此处假设从缓存里'''
        return
