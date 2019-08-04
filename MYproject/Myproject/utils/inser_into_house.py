import os
import sys
import random
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Myproject.settings.dev")
import django
django.setup()
from home import  models
with open("fangziinfo.txt","rt") as f :
    for i  in f :
        l=i.split("|").__iter__()

        while True:
            yuanjia=next(l)[0:4]
            title=next(l)
            size=next(l)
            orientations=next(l)
            level=next(l)
            xiaoqu=next(l)
            xianjia=str(int(yuanjia)+100)
            i=random.randrange(0,9999999)
            reg=models.Housing_estate.objects.filter(name=xiaoqu)
            if not reg :
                xiaoqu_obj=models.Housing_estate.objects.create(name=xiaoqu,xiaozheng_id=random.randint(1,17),ditie_id=random.randint(1,7),transportation_id=random.randint(1,3))
            else :
                xiaoqu_obj=reg.first()
            Expenses_obj=models.Expenses.objects.filter(id=random.randint(1,4)).first()
            user=models.Housing.objects.create(room_id=i,title=title,size=size,xiaoqu=xiaoqu_obj,xianjia=xianjia,orientation=random.randint(1,4),level=level,hot=random.randint(0,1000),zhoubian_id=random.randint(1,3),fangdong_id=1)
            user.expenses.add(Expenses_obj)
            user.allocation.add(*[random.randint(1, 3) for i in range(3)])
            user.save()




