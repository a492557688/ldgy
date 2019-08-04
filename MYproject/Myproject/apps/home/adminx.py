import xadmin
from xadmin import views
from . import models
from .models import *
xadmin.autodiscover()
class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "路飞学城"  # 设置站点标题
    site_footer = "路飞学城有限公司"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠
#
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(Nav_title)
xadmin.site.register(Nav)
xadmin.site.register(Banner)
xadmin.site.register(Area)
xadmin.site.register(Zhoubian)
xadmin.site.register(Town)
xadmin.site.register(Housing)
xadmin.site.register(Housing_img)
xadmin.site.register(Kuaixun)
xadmin.site.register(Expenses)
xadmin.site.register(Activity)
xadmin.site.register(Ditie)
xadmin.site.register(Allocation)
# xadmin.site.register()
xadmin.site.register(Housing_estate)
xadmin.site.register(Fangdong)
xadmin.site.register(Room_type)
xadmin.site.register(Transportation)

xadmin.site.register(other_Room_details)
# xadmin.site.register(Room_type)
# xadmin.site.register(Nav)
# xadmin.site.register(Nav)