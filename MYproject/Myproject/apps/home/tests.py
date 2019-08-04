from django.test import TestCase

# Create your tests here.

if __name__ == '__main__':
    import os
    import sys
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Myproject.settings.dev")

    import django
    django.setup()
    from django.core.cache import cache
    from django_redis import get_redis_connection
    conn = get_redis_connection()
    conn.set("jrth","[2,3,4]",3600*24)

    # from home import models
    #
    # towns = " 北蔡	碧云	 曹路	川沙	 高东	高行	 花木	合庆	航头	 金桥	金杨	 康桥	 陆家嘴	联洋	 南码头	 世博	三林	 塘桥	唐镇	 潍坊	外高桥	新场	 杨东 洋泾	御桥	源深	 张江	周浦"
    # towns=towns.split(" ")
    # towns=[t.strip() for t in towns]
    # for i in towns:
    #     models.Town.objects.create(name=i,area_id=3)
