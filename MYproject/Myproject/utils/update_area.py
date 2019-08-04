import os
import sys
import random
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Myproject.settings.dev")
import django
django.setup()

from home import  models
xiaozheng_list=list(models.Town.objects.all())
for xiaozheng in xiaozheng_list :
    xiaozheng.area_id=random.randint(1,32)
    xiaozheng.save()