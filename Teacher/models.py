from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser


# Create your models here.
'''
class User(AbstractUser):
    tiGender = models.IntegerField,  # 1=male,2=female,3=other
    dtDOB = models.IntegerField,
    stGovIDNo = models.CharField(max_length=10),
    tiBloodgroup = models.IntegerField,  # 1=A+,2=A-,3=B+,4=B-,5=O+,6=O-,7=AB+,8=AB-
    inReligion = models.IntegerField,  # 1=Islam,2=Hindu,3=Christian,4=Buddish,5=Others
    stClass = models.CharField(max_length=50, null=True, blank=True),
    inSection = models.IntegerField,
    stAddress = models.CharField(max_length=1000, null=True, blank=True),
    stPhone = models.CharField(max_length=40, null=True, blank=True),
    stPhotoPath = models.CharField(max_length=2000, null=True, blank=True)
    stshortBIO = models.CharField(max_length=2000, null=True, blank=True)
    tiUserType = models.IntegerField,
    stOccupation = models.CharField(max_length=100, null=True, blank=True),
    flgIsDeleted = models.BooleanField
    dtModifyDate = models.DateTimeField
    inModifyBy = models.IntegerField
    inCreateBy = models.IntegerField'''

'''class User_Master(models.Model):
    inID = models.IntegerField,
    stFName = models.CharField(max_length=100),
    stLName = models.CharField(max_length=100),
    tiGender = models.IntegerField,      #1=male,2=female,3=other
    dtDOB = models.IntegerField,
    stGovIDNo = models.CharField(max_length=10),
    tiBloodgroup = models.IntegerField,  #1=A+,2=A-,3=B+,4=B-,5=O+,6=O-,7=AB+,8=AB-
    stReligion = models.IntegerField,    #1=Islam,2=Hindu,3=Christian,4=Buddish,5=Others
    stEmail = models.CharField(max_length=100),
    stClass = models.CharField(max_length=100),
    inSection = models.IntegerField,
    stAddress = models.CharField(max_length=1000),
    stPhone = models.CharField(max_length=10),
    stshortBIO = models.CharField(max_length=2000)'''
