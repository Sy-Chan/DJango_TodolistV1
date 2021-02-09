from django.db import models

# Create your models here.
class ToDo_List(models.Model):
    date = models.DateField("Date Created", auto_now=False, auto_now_add=True)
    action = models.CharField("What to do?", max_length=200)
    due = models.DateField("Due Date", auto_now=False, auto_now_add=False,)
    status = models.BooleanField("Done", default = False)
    dDate = models.DateField("Done on",null=True, blank=True, auto_now=False, auto_now_add=False)
