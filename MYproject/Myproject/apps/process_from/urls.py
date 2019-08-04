from django.conf.urls import url
from Myproject.apps.process_from import views
from django.contrib import admin

urlpatterns = [
url(r'submit_fwtg/',views.Submit_fwtg.as_view())
]
