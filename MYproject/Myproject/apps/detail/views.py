from django.shortcuts import render
from home import  models
from rest_framework.generics import ListAPIView
from home import serializer
from rest_framework.response import  Response
# Create your views here.
class Detail_hour(ListAPIView):
    queryset = models.Housing.objects.filter(is_dele=0, is_show=1)
    serializer_class = serializer.Detail_hourSerializer
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(id=request.GET.get("id"))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)