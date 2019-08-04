from rest_framework.serializers import  ModelSerializer
from rest_framework import serializers
from home import models
# class Nav_title(ModelSerializer):
#     class Meta:
#         fields=["title","name","nav_url","nav_ordering"]
#         model=models.Nav


class NavSerializer(ModelSerializer):
    class Meta:
        # fields=["name","rank"],
        fields=["name","rank","content"]
        model=models.Nav_title

class  BennerSerializer(ModelSerializer):
    class Meta:
        fields=["img","banner_url","ordering"]
        model=models.Banner





class Housing_estateSerializer(ModelSerializer):
    class Meta:
        fields = ["name"]
        model = models.Area
class Room_typeSerializer(ModelSerializer):
    class Meta:
        fields = ["name","xuanchuan_img","url"]
        model = models.Room_type
class Town(ModelSerializer):
    class Meta:
        fields = ["name"]
        model = models.Town

class xiaoquSerializer(ModelSerializer):
    xiaozheng =Town()
    class Meta:
        fields = ["name","xiaozheng"]
        model = models.Housing_estate

class zhoubianSerializer(ModelSerializer):
    class Meta:
        fields = ["name"]
        model = models.Zhoubian

class  AreaSerializer(ModelSerializer):
    town_set=Town(many=True)
    class Meta:
        fields=["name","town_set"]
        model=models.Area
        depth=1


class hourseSerializer(ModelSerializer):
    xiaoqu=xiaoquSerializer()
    expenses = serializers.SerializerMethodField()
    def get_expenses(self,obj):
        query_set=obj.expenses.all()
        l=[]
        for i in query_set:
            l.append(i.name)
        return l
    zhoubian=zhoubianSerializer()
    area1 = serializers.CharField(source="xiaoqu.xiaozheng.area")
    ditie_id=serializers.CharField(source="xiaoqu.ditie.id")
    class Meta:
        fields = ["id","room_id","xiaoqu","zhoubian","xianjia","first_img","area1","ditie_id","town","expenses"]
        model = models.Housing
        depth =2





class other_Room_detailsSerializer(ModelSerializer):
    class Meta:
        fields =["or_id","price","get_state_display","expiration_Date","have_windows","have_yangtai","have_selfwc"]
        model=models.other_Room_details
class fangdongSerializer(ModelSerializer):
    class Meta:
        fields =["name","sum_chuzu","recently_sum_chuzu"]
        model = models.Fangdong
class expensesSerializer(ModelSerializer):
    class Meta:
        fields =["name"]
        model = models.Expenses
class transportationserializers(ModelSerializer):
    class Meta:
        fields =["name"]
        model = models.Expenses


class Detail_hourSerializer(ModelSerializer):
    # xiaoqu=xiaoquSerializer()
    zhoubian=zhoubianSerializer()
    # other_Room_details=other_Room_detailsSerializer()
    # expenses=expensesSerializer()

    fangdong=fangdongSerializer()
    xiaoqu = serializers.CharField(source="xiaoqu.name")
    expenses=serializers.SerializerMethodField()
    transportation=transportationserializers()

    def get_expenses(self,obj):
        query_set=obj.expenses.all()
        l=[]
        for i in query_set:
            l.append(i.name)
        return l

    allocation = serializers.SerializerMethodField()
    # area = serializers.CharField(source="xiaoqu.name")
    town = serializers.CharField(source="xiaoqu.xiaozheng")
    area = serializers.CharField(source="xiaoqu.xiaozheng.area")
    def get_allocation(self, obj):

        query_set = obj.allocation.all()
        l = []
        for i in query_set:
            l.append(i.name)
        return l

    #


            # fields = ["or_id", "price", "get_state_display", "expiration_Date", "have_windows", "have_yangtai",
            #           "have_selfwc", "protocol", ]




    other_Room_details1=other_Room_detailsSerializer(many=True)
    class Meta:

        fields = ["id","area","protocol","town","other_Room_details1","hourseimg_list","room_id","title","xianjia","hot","yuanjia","size","get_orientation_display","level","zhoubian","expenses","fangdong","allocation","xiaoqu","transportation"]
        # fields="__all__"
        model = models.Housing
        depth = 1