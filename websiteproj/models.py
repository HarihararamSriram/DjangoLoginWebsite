from django.db import models

# Create your models here.
class User_of_ocean(models.Model):
    """
    This is class contains the attributes of the user
    """
    uname = models.CharField(max_length=100, primary_key=True, null=False, blank=False,\
                             verbose_name="Username")
    name = models.CharField(max_length=100, null=False, blank=False,\
                             verbose_name="Name")
    dob = models.DateField(null=False, blank=False,\
                             verbose_name="Date")
    password = models.CharField(max_length=100, null=False, blank=False,\
                             verbose_name="Password")
    
