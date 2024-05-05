from django.db import models

# Create your models here.

class Library(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    semester = models.IntegerField() 
    quantity = models.IntegerField()
    price = models.IntegerField()
    

class datamember(models.Model):
    name=models.CharField(max_length=40)
    mobile=models.IntegerField()
    semester=models.IntegerField()
    branch=models.CharField(max_length=40)    


class Records(models.Model):
    member_id = models.ForeignKey(datamember, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Library, on_delete=models.CASCADE)
    issue_date = models.DateField()
    return_date = models.DateField()
    status = models.CharField(max_length=200)

