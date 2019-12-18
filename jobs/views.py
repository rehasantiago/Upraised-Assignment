import csv,io
import pandas as pd
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import Skill
from .skills_extraction import Skill_extract
import datetime
from django.db.models import Q
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from datetime import date
from dateutil.relativedelta import relativedelta
import json
# Create your views here.

def date_convertor(s):
    if "month" in s:
        number = int(s.split()[0])
        date = pd.datetime.now()-pd.DateOffset(months=number)
    elif "week" in s:
        number = int(s.split()[0])
        date = pd.datetime.now()-pd.DateOffset(weeks=number)
    elif "just" in s:
        date=pd.datetime.now()
    else:
        number = int(s.split()[0])
        date = pd.datetime.now()-pd.DateOffset(hours=number)
    return date


@permission_required('admin.can_add_log_entry')
def upload(request):
    template = "upload.html"

    if request.method=="GET":
        return render(request,template)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        message.error(request,'This is not a csv file')
    
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    sk = Skill_extract()

    for row in csv.reader(io_string,delimiter=','):
        date=date_convertor(row[3])
        _,created = Skill.objects.get_or_create( 
            title=row[0], 
            description=row[1], 
            company=row[2], 
            skills_required=sk.process(row[1]),
            created_date=datetime.datetime(date.year,date.month,date.day,date.hour,date.minute,date.second,date.microsecond)
            ) 
    context={}
    return render(request,template,context)

def jobs(request,value):
    data = Skill.objects.filter(created_date__month__gte=datetime.datetime.today().month-1).filter(Q(title__icontains=value) | Q(skills_required__icontains=value) | Q(description__icontains=value))
    return HttpResponse(serializers.serialize("json", data), content_type="text/json-comment-filtered")

def job_search(request,**kwargs):
    d1=datetime.datetime(kwargs['year1'],kwargs['month1'],kwargs['day1'],kwargs['hour1'],kwargs['minute1'],kwargs['second1'])
    d2=datetime.datetime(kwargs['year2'],kwargs['month2'],kwargs['day2'],kwargs['hour2'],kwargs['minute2'],kwargs['second2'])
    if(d1<datetime.datetime.today() - datetime.timedelta(days=30)):
        d1=datetime.datetime.today() - datetime.timedelta(days=30)
    print(d1)
    data1 = json.loads(serializers.serialize("json",Skill.objects.filter(created_date__range=[d1,d2])))
    data2 = json.loads(serializers.serialize("json",Skill.objects.filter(created_date__range=[d1,d2]).order_by('title')))
    data3 = json.loads(serializers.serialize("json",Skill.objects.filter(created_date__range=[d1,d2]).order_by('company')))
    skills_json={}
    for skill in ['sales skills','math','punctuality','negotiation skills','communication','problem solving','management','structured thinking','prioritization','finance','data modeling and analysis','basic tools of product management','understanding of technical concepts','marketing','sports and outdoors','organizational abilities','disabled veteran and minority']:
        skills_json[skill]=json.loads(serializers.serialize("json",Skill.objects.filter(created_date__range=[d1,d2]).filter(skills_required__icontains=skill)))
    data={
        "total jobs":data1,
        "grouped by title":data2,
        "grouped by company":data3,
        "grouped by skill":skills_json
    }
    return JsonResponse(data)