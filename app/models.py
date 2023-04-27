from django.db import models

# Create your models here.


class Topic(models.Model):
    Sid=models.IntegerField(primary_key=True)
    Topic_Name=models.CharField(max_length=100)
   

    def __str__(self):
        return self.Topic_Name
    
class Webpage(models.Model):
    Topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    Url=models.URLField()
    Email=models.EmailField(default='Sbharath143@gmail.com')
    Mobilenumber=models.IntegerField()

    def __str__(self):
        return self.Name
    
class AccessRecord(models.Model):
    Name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    Author=models.CharField(max_length=100)
    Date=models.DateTimeField()

    def __str__(self):
        return self.Author


