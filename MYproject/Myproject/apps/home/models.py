from Myproject.utils.models import BaseModel
from django.db import models
from django.contrib.auth.models import  AbstractUser
class MyUser(AbstractUser):
    mobile=models.BigIntegerField
    def __str__(self):
        return self.username
class  Nav_title(BaseModel):
    name=models.CharField(max_length=32)
    rank = models.IntegerField(default=0)
    def __str__(self):
        return self.name
    @property
    def content(self):
        nav_list=[]
        for nav in self.nav.all():
            nav_list.append({"title":nav.name,"nav_url":nav.nav_url,"ordering":nav.nav_ordering})
        return  nav_list

class  Nav(BaseModel):
    title=models.ForeignKey(to=Nav_title,on_delete=models.DO_NOTHING,related_name="nav")
    name = models.CharField(max_length=32)
    nav_url=models.CharField(max_length=32)
    nav_ordering=models.IntegerField()
    def __str__(self):
        return self.name

class Banner(BaseModel):
    name=models.CharField(max_length=32)
    img=models.FileField(upload_to="banner")
    banner_url=models.CharField(max_length=500)
    ordering=models.IntegerField()
    def __str__(self):
        return self.name
class  Area(BaseModel):
    '''行政区表'''
    name=models.CharField(max_length=32)
    hot=models.IntegerField(default=0)
    def __str__(self):
        return self.name
class Town(BaseModel):
    '''小镇表'''
    name=models.CharField(max_length=32)
    area=models.ForeignKey(to="Area",on_delete=models.DO_NOTHING)
    hot=models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Zhoubian(BaseModel):
    name=models.CharField(max_length=32)
    def __str__(self):
        return self.name

class Ditie(BaseModel):
    name=models.CharField(max_length=32)

class Transportation(BaseModel):
    name = models.CharField(max_length=32)

    # @property
    # def get_name(self):
    #     return str(self.id)+"号线"
    #
    # name = models.CharField(default=get_name,max_length=65)
class Housing_estate(BaseModel):
    '''小区表'''
    name=models.CharField(max_length=32)
    addr=models.CharField(max_length=32)
    xiaozheng=models.ForeignKey(to="Town",on_delete=models.DO_NOTHING)
    zhoubian=models.ManyToManyField(to="Zhoubian")
    ditie=models.ForeignKey(to=Ditie,on_delete=models.DO_NOTHING)
    transportation=models.ForeignKey(to=Transportation,on_delete=models.DO_NOTHING)
    hot=models.IntegerField(default=0)
    def __str__(self):
        return self.name
class  Room_type(BaseModel):
    name=models.CharField(max_length=32)
    xuanchuan_img=models.FileField(upload_to="Room_type")
    url=models.CharField(max_length=32)
    def __str__(self):
        return self.name

class Housing_img(BaseModel):
    img_url=models.CharField(max_length=256)
    the_hourse=models.ForeignKey(to="Housing",on_delete=models.DO_NOTHING,related_name="housing_img",db_constraint=False)
    the_hourse_img=models.FileField(upload_to="housing")
    is_first=models.BooleanField(default=False)


class Housing(BaseModel):
    room_id=models.CharField(max_length=15)
    title=models.CharField(max_length=64)
    xiaoqu=models.ForeignKey(to=Housing_estate,on_delete=models.DO_NOTHING)
    xianjia = models.IntegerField()
    zhoubian=models.ForeignKey(to=Zhoubian,on_delete=models.DO_NOTHING)
    hot = models.IntegerField()
    update_data=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.room_id
    @property
    def hourseimg_list(self):
        hourseimg_list=[]
        for i in self.housing_img.all():
            hourseimg_list.append({"url":i.img_url,"img_file":str(i.the_hourse_img)})
        return hourseimg_list
    @property
    def first_img(self):
        try:
            return str(self.housing_img.all().filter(is_first=True).first().the_hourse_img)
        except Exception as f :
            print(f)
            return [1]
    @property
    def area(self):
        return self.xiaoqu.xiaozheng.area
    @property
    def town(self):
        return self.xiaoqu.xiaozheng.name



    # <!--详细信息-->
    @property
    def addr(self):
        return self.xiaoqu.addr

    expenses = models.ManyToManyField(to="Expenses")
    yuanjia=models.IntegerField
    allocation=models.ManyToManyField(to="Allocation")
    size=models.CharField(max_length=64)
    orientations=((1,"朝南"),(2,"朝北"),(3,"朝东"),(4,"朝西"))
    orientation=models.IntegerField(choices=orientations)
    level=models.CharField(max_length=64)
    # now_price = models.IntegerField)

    #other_Room_details=models.ForeignKey(to="other_Room_details",on_delete=models.DO_NOTHING)



    @property
    def ditie(self):
        return self.xiaoqu.ditie.name

    def transportation(self):
        return  self.xiaoqu.transportation

    @property
    def zhoubian_list(self):
        que=self.xiaoqu.zhoubian.all()
        l=[]
        for i in que:
            l.append(i.name)
        return  l

    fangdong=models.ForeignKey(to="Fangdong",related_name="fangzi",on_delete=models.DO_NOTHING,db_constraint=False)
    protocol = models.TextField()

    @property
    def  other_Room_details1(self):
        return  self.other_Room_details.all()

        # l = []
        # for i in self.other_Room_details.all():
        #     l.append(
        #         {
        #             "or_id": i.or_id,
        #             "price": i.price,
        #             "get_state_display": i.get_state_display,
        #             "expiration_Date": i.expiration_Date,
        #             "have_windows": i.have_windows,
        #             "have_yangtai": i.have_yangtai,
        #             "have_selfwc": i.have_selfwc,
        #         })
        # return l


class Fangdong(BaseModel):
    name=models.CharField(max_length=256)
    sum_chuzu=models.IntegerField()
    recently_sum_chuzu=models.IntegerField()
    @property
    def home_count(self):
        return self.fangzi.count()





class Allocation(BaseModel):
    name=models.CharField(max_length=256)





class Expenses(BaseModel):
    name=models.CharField(max_length=256)
    def __str__(self):
        return self.name


class Kuaixun(BaseModel):
    title=models.CharField(max_length=20)
    content=models.TextField()
    kuaixun_img=models.CharField(max_length=15)


class other_Room_details(BaseModel):
    hous=models.ForeignKey(to=Housing,db_constraint=False,on_delete=models.DO_NOTHING,related_name="other_Room_details")
    or_id=models.CharField(max_length=20)
    price=models.IntegerField()
    stat=((1,"已租"),(2,"空闲"))
    state=models.IntegerField(choices=stat)
    expiration_Date=models.DateTimeField()
    have_windows=models.BooleanField()
    have_yangtai=models.BooleanField()
    have_selfwc=models.BooleanField()
    # protocol=mod/els.TextField()







# class Housing_Details(BaseModel):
#     video_url = models.CharField(max_length=256)
#     huodong_now=models.ForeignKey(to="Activity",on_delete=models.DO_NOTHING)
#     yuanjia=models.IntegerField()
#     area=models.IntegerField()
#     taiyang=((1,"朝北"),(2,"朝南"),(3,"朝东"),(4,"朝西"))
#     chaoxiang=models.IntegerField(choices=taiyang)
#     louceng=models.IntegerField()
#




    # name=models.CharField(max_length=125,default=)
class Activity(BaseModel):
    name=models.CharField(max_length=257)
    content=models.TextField()
    def __str__(self):
        return self.name
