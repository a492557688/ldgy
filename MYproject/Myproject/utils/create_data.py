import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Myproject.settings.dev")
import django
django.setup()
from home.models import Area,Housing_estate
l=[
'旭辉城租房',
'崧泽绿地租房',
'沁富佳苑租房',
'松江登云苑租房',
'宝山佳境苑租房',
'德宁苑租房',
'唐家苑租房',
'金海华城永华苑租房',
'张江樟盛苑租房',
'登云苑租房',
'塘泾南苑租房',
'馨香三期灯辉公寓租房',]
import datetime
import time
for i in l:
    Housing_estate.objects.create(name=i)

# q=Area.objects.all()
# q.update(is_show=1)
# q.update()
# if __name__ == '__main__':
#     s="旭辉城租房 | 崧泽绿地租房 | 沁富佳苑租房 | 松江登云苑租房 | 宝山佳境苑租房 | 德宁苑租房 | 唐家苑租房 | 金海华城永华苑租房 | 张江樟盛苑租房 | 登云苑租房 | 塘泾南苑租房 | 馨香三期灯辉公寓租房"
#     for i in s.split(" | "):
#         print(i)