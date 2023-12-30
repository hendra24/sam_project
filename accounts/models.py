from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete
import os
# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError("ENTER A VALID EMAIL !!")
        if not username:
            raise ValueError("USER MUST HAVE USERNAME !!")
        
        user = self.model (
            email = self.normalize_email(email),
            username = username,
            first_name = first_name, 
            last_name = last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name, 
            last_name = last_name
        )
        
        user.is_active = True 
        user.is_admin = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    role = models.ForeignKey('Role',on_delete=models.SET_NULL, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    
    objects = MyAccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True

class Role(models.Model):
    role_name = models.CharField(max_length=50)
    is_all = models.BooleanField(default=False)
    is_create = models.BooleanField(default=False)
    is_retrieve = models.BooleanField(default=False)
    is_update = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.role_name
    
class Profile(models.Model):
    user = models.OneToOneField('Account',on_delete=models.CASCADE)
    phone_number = models.IntegerField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='userprofile', blank=True, null=True)
    company  = models.ForeignKey('Company', blank=True,null=True,on_delete=models.SET_NULL)
    division = models.ForeignKey('Division', blank=True, null=True,on_delete=models.SET_NULL)
    position = models.ForeignKey('Position', blank=True, null=True,on_delete=models.SET_NULL)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True) 
    
    # Signal to create a Profile when a Account is created
    @receiver(post_save, sender=Account)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    
    def __str__(self):
        return self.user.email
     
    


class Company(models.Model):
    company_name = models.CharField(max_length=100, unique=True)
    company_address = models.CharField(max_length=250,  blank=True, null=True)
    company_description = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.company_name
    
class Division(models.Model):
    division_name = models.CharField(max_length=100, unique=True)
    division_description = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.division_name


class Position(models.Model):
    position_name = models.CharField(max_length=100, unique=True)
    position_description = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.position_name