"""upraised_assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from jobs.views import upload,jobs,job_search

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('upload/',upload,name="upload"),
    path('jobs/<str:value>/',jobs,name="jobs"),
    path('startdate/<int:year1>-<int:month1>-<int:day1>-<int:hour1>-<int:minute1>-<int:second1>/enddate/<int:year2>-<int:month2>-<int:day2>-<int:hour2>-<int:minute2>-<int:second2>/',job_search,name="job_search")
]
