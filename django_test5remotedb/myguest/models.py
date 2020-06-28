from django.db import models

# Create your models here.
class Guest(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField() 
    regdate = models.DateTimeField()
    
    
    class Meta:
        #ordering = ('title',)  #반드시 튜플이어야한다
        ordering = ('-id',)
    
    
