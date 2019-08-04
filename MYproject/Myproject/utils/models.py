from  django.db import  models

class BaseModel(models.Model):
    create_time=models.DateTimeField(auto_now_add=True)
    is_show = models.BooleanField(default=True)
    is_dele = models.BooleanField(default=False)
    class Meta:
        abstract=True