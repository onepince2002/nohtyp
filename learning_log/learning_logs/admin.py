from django.contrib import admin

# Register your models here.
from learning_logs.models import Topic,Entry # 新增區塊
admin.site.register(Topic)
admin.site.register(Entry) # 新增區塊

