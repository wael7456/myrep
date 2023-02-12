from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager , PermissionsMixin
from django.contrib.auth.models import UserManager


class MyAccountManager (BaseUserManager):
    def create_user ( self, email, username, first_name, last_name, password , **other_fields):
        if not email :
            raise ValueError('users must has an email adress')
        if not username :
            raise ValueError('users must has a username ')
        email=self.normalize_email(email)
        user=self.model(
            email= email ,
            username= username ,
            first_name=first_name, 
            last_name=last_name,
            **other_fields )
            
            
    
        user.set_password(password)
        user.save()
        return user 
    

    def create_superuser (self, email, username, first_name,last_name , password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active',True)

        if other_fields.get('is_staff') is not True :
            raise ValueError(
                'Superuser must be assigned to is_staff=True')
            
        if other_fields.get('is_superuser') is not True :
            raise ValueError(
                'Superuser must be assigned to is_superuser=True')
        return self.create_user(email, username, first_name,last_name, password, **other_fields  )   




class CustomUser(AbstractBaseUser , PermissionsMixin):
    
    email  = models.EmailField(verbose_name="email", max_length=60, unique=True)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default= False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    password = models.CharField(max_length=50)
    #password2 = models.IntegerField()
    username =models.CharField(max_length=40 , unique= True)
    last_name=models.CharField(max_length=40 , blank= True)
    first_name=models.CharField(max_length=40 , blank= True) 
    


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']
     
    objects= MyAccountManager()


    def __str__(self) :
        return self.email 


    #def has_perm(self, perm , obj= None):
       # return self.is_superuser

    #def has_module_perms(self, app_label ) :
        #return True

