
import os
import sys
import random
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Myproject.settings.dev")
import django
django.setup()
from home import  models
s="/detail/house_info/?id="
import os
path=r"C:\Users\MYproject\Myproject\media\db"
hour_list=list(models.Housing.objects.all())
wenjian=os.listdir(path)
wenjian=["hours/"+i for i in wenjian]
for i in wenjian:
    hour=random.choice(hour_list)
    if hour.housing_img.all().filter(is_first=True):
        is_filrst=False
    else :

        is_filrst = True
    models.Housing_img.objects.create(img_url=s+str(hour.id),the_hourse=hour,the_hourse_img=i,is_first=is_filrst)
    # break

# if __name__ == '__main__':
#     hour = random.choice(hour_list)
#     reg=hour.housing_img.all().filter(id=is_first=True)
#     print(reg)