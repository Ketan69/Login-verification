from django.db import models

class id(models.Model):
 loginid=models.EmailField(primary_key=True,max_length=20,default='')
 password=models.EmailField(max_length=20,default='')
 name=models.EmailField(max_length=20,default='')
 emailid=models.EmailField(max_length=50,default='')
 cellno=models.BigIntegerField(default=0)
 
