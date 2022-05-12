from django.db import models

# Create your models here.

class Task(models.Model):
    title=models.CharField(max_length=200) 
    complete=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title 


#Can we agree that the field we want for now is the one named title?...yes
#So we go into the template tags and do the follwing