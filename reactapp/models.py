from django.db import models


class Parent(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    
    def __str__(self):
        return self.name
    
class Children(models.Model):
   parent = models.ForeignKey(
        Parent, related_name='parents', on_delete=models.CASCADE)
   mobile = models.CharField(max_length=100,blank=True,null=True)
   def __str__(self):
        return self.mobile
   
   
   
   

class CategoryModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    backgroundColor = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class Album(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=4000)
    price = models.IntegerField(default=10)
    categoryId = models.IntegerField(default=1)
    userId = models.IntegerField(default=1)

    def __str__(self):
        return self.title


class IImage(models.Model):
    album = models.ForeignKey(
        Album, related_name='images', on_delete=models.CASCADE)
    url = models.CharField(max_length=300,null=True,blank=True)
    thumbnailUrl = models.CharField(max_length=300,null=True,blank=True)
    aimage = models.ImageField(upload_to='photos', default='default.jpg')
    bimage = models.ImageField(upload_to='photos', default='default.jpg')

    def __str__(self):
        return self.url


class Location(models.Model):
    album = models.ForeignKey(
        Album, related_name='locations', on_delete=models.CASCADE)
    latitude = models.IntegerField(default=1)
    longitude = models.IntegerField(default=2)

class Payment (models.Model):
    album = models.ForeignKey(
        Album, related_name='payments', on_delete=models.CASCADE)
    payment1 = models.CharField(max_length=300,blank=True,null=True,default="Bkash")
    payment2 = models.CharField(max_length=300,blank=True,null=True,default="Nagad")
    payment3 = models.CharField(max_length=300,blank=True,null=True,default="Rocket")
    payment4 = models.CharField(max_length=300,blank=True,null=True,default="Bank1")
    payment5 = models.CharField(max_length=300,blank=True,null=True,default="Bank2")
    payment6 = models.CharField(max_length=300,blank=True,null=True,default="Bank3")
    payment7 = models.CharField(max_length=300,blank=True,null=True,default="Bank4")
    payment8 = models.CharField(max_length=300,blank=True,null=True,default="others")
    
class Other (models.Model):
    album = models.ForeignKey(
        Album, related_name='others', on_delete=models.CASCADE)
    other1 = models.CharField(max_length=100,blank=True,null=True,default="some")
    other2 = models.CharField(max_length=100,blank=True,null=True,default="some")
    other3 = models.CharField(max_length=100,blank=True,null=True,default="some")
    other4 = models.CharField(max_length=100,blank=True,null=True,default="some")
    other5 = models.CharField(max_length=100,blank=True,null=True,default="some")
    other6 = models.CharField(max_length=100,blank=True,null=True,default="some")
    other7 = models.CharField(max_length=100,blank=True,null=True,default="some")
    other8 = models.CharField(max_length=100,blank=True,null=True,default="some")
    

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)
    aimage = models.ImageField(upload_to='photos', default='default.jpg')
    price = models.IntegerField(default=100,blank=True, null=True)
    category = models.IntegerField(default=2,blank=True, null=True)
    description = models.TextField(null=True,blank=True)
    latitude = models.CharField(max_length=100,default='0',blank=True,null=True)
    longitude = models.CharField(max_length=100,default='0',blank=True,null=True)
    

    def __str__(self):
        return self.title
    
    
    
#this a message model Api
class Msg(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    
    completed = models.BooleanField(default=False, blank=True, null=True)
    aimage = models.ImageField(upload_to='photos', default='default.jpg')

    
    

    def __str__(self):
        return self.title    


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
