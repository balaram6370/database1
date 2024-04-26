from django.db import models




# Create your models here.

class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)
    email_id=models.EmailField(max_length=100,default='ipl2024@gmail.com')

    def __str__(self):
        return self.topic_name



class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()

    def __str__(self):
        return self.name

    

class AcessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    data=models.DateField()
    author=models.CharField(max_length=100)

    def __str__(self):
        return self.author
