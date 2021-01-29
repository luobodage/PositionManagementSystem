from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from jobs.models import Job
from jobs.models import Cities, JobTypes


# Create your views here.

def joblist(request):
    job_list = Job.objects.order_by('job_type')  # 直接从数据库取数据 这是django models的语法
    template = loader.get_template('joblist.html')  # 加载模板
    context = {'job_list': job_list}

    for job in job_list:
        job.city_name = Cities[job.job_city][1]  # 取出对应城市的信息
        job.type_name = JobTypes[job.job_type][1] # 去除对应工作信息
    return HttpResponse(template.render(context))  # 用模板的render方法把上下文展现出来
