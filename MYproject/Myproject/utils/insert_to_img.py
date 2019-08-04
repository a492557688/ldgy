import redis
pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)
import requests
import os
import sys
import random
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Myproject.settings.dev")
import django
django.setup()

while 1 :
    url = r.lpop("img_list").decode()
    file_name=url.split("/")[-1]
    res = requests.get(url).content
    file_path="D:\sss\{}" .format(file_name)
    with open(file_path, "wb") as w:
        w.write(res)