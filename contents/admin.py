from django.contrib import admin

# Register your models here.
from contents.models import NoticeList,HospitalList
admin.site.register(NoticeList)
admin.site.register(HospitalList)
