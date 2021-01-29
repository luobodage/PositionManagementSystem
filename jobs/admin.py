from django.contrib import admin
from jobs.models import Job


# Register your models here.

class JobAdmin(admin.ModelAdmin):
    # 隐藏并自动生成
    exclude = ('creator', 'created_date', 'modified_date')
    # 主页面显示
    list_display = ('job_name', 'job_type', 'job_city', 'job_duty', 'creator', 'created_date', 'modified_date')

    # 创建人自动生成为登录用户User
    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Job, JobAdmin)
