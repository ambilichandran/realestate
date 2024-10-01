from django.db import models
class Service(models.Model):
    name=models.CharField(max_length=100,blank=None)
    image=models.ImageField(upload_to="image")
    description=models.TextField(max_length=300,blank=True)
    def __str__(self):
        return self.name
class About(models.Model):
    name=models.ForeignKey(Service,on_delete=models.CASCADE)
    description= models.TextField(max_length=300,blank=None) 
    def ___str__(self):
        return self.name   
class Team(models.Model):
    name=models.CharField(max_length=50,blank=None)
    image=models.ImageField(upload_to="image")
    qualification=models.CharField(max_length=150,blank=None)
    def __str__(self):
        return self.name
class Form(models.Model):
    name=models.CharField(max_length=50,blank=None)
    address=models.TextField(max_length=300,blank=None)
    phone=models.IntegerField()
    property_type=models.ForeignKey(Service,on_delete=models.CASCADE)
    district=models.CharField(max_length=50,blank=None)
    locality=models.CharField(max_length=50,blank=True)
    condition=models.TextField(max_length=300,blank=True)
    def __str__(self):
        return self.name 
class Comment(models.Model):
    client_name=models.CharField(max_length=50,blank=None)
    image=models.ImageField(upload_to="image")
    comment=models.TextField(max_length=300,blank=None)   
    profession=models.CharField(max_length=50,blank=None)
    def __str__(self):
        return self.client_name
