from django.db import models

# Create your models here.
class Skill(models.Model): 
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    company = models.CharField(max_length=100) 
    skills_required = models.CharField(max_length=150,null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=False,auto_now=False,blank=True,null=True)
    def __str__(self):
        return self.title