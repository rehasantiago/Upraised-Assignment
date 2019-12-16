import csv,io
import pandas as pd
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import Skill
from .skills_extraction import Skill_extract
import datetime
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
