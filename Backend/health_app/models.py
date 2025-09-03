# type:ignore
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.validators import MaxValueValidator
from django.db import models


class UserProfile(AbstractUser):
    # email = models.EmailField(blank=False, null=False)
    dateOfBirth = models.DateField(null=True)

    # Gender
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    mobileNumber = models.CharField(max_length=17, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    first_name = models.CharField(max_length=200, null=True)
    middle_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)

    address = models.CharField(max_length=300)
    # profile_pic = models.ImageField(null=True, blank=True)

    class Meta:
        pass
        # abstract = True

    def __str__(self):
        return self.username


class Patient(UserProfile):

    # Blood group
    A_POSITIVE = 'A+'
    A_NEGATIVE = 'A-'
    B_POSITIVE = 'B+'
    B_NEGATIVE = 'B-'
    AB_POSITIVE = 'AB+'
    AB_NEGATIVE = 'AB-'
    O_POSITIVE = 'O+'
    O_NEGATIVE = 'O-'

    BLOOD_GROUP_CHOICES = [
        (A_POSITIVE, 'A+'),
        (A_NEGATIVE, 'A-'),
        (B_POSITIVE, 'B+'),
        (B_NEGATIVE, 'B-'),
        (AB_POSITIVE, 'AB+'),
        (AB_NEGATIVE, 'AB-'),
        (O_POSITIVE, 'O+'),
        (O_NEGATIVE, 'O-'),
    ]
    bloodGroup = models.CharField(
        max_length=4, choices=BLOOD_GROUP_CHOICES, null=True)
    isSpecialDisease = models.BooleanField(null=True)

    # ************************************************************************************************************************************************************************************************************************
    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'date_of_birth', 'gender', 'address', 'phone_number']
    # ************************************************************************************************************************************************************************************************************************

    # diseases=models.ManyToManyField()


class Doctor(UserProfile):
    experience = models.IntegerField(validators=[MaxValueValidator(50)],default=0)

    MBBS = 'MBBS'
    MD = 'MD'
    DO = 'DO'
    DNB = 'DNB'
    MS = 'MS'
    BDS = 'BDS'
    MDS = 'MDS'
    PhD = 'PhD'
    MPH = 'MPH'
    DM = 'DM'
    MCh = 'MCh'
    BAMS = 'BAMS'
    BHMS = 'BHMS'
    BPT = 'BPT'
    MPT = 'MPT'
    BVSc = 'BVSc'
    MSc = 'MSc'
    DGO = 'DGO'
    FRCS = 'FRCS'
    MRCP = 'MRCP'
    DCH = 'DCH'
    DPH = 'DPH'
    DDS = 'DDS'
    DEGREE_CHOICES = [
        (MBBS, 'MBBS'),
        (MD, 'MD'),
        (DO, 'DO'),
        (DNB, 'DNB'),
        (MS, 'MS'),
        (BDS, 'BDS'),
        (MDS, 'MDS'),
        (PhD, 'PhD'),
        (MPH, 'MPH'),
        (DM, 'DM'),
        (MCh, 'MCh'),
        (BAMS, 'BAMS'),
        (BHMS, 'BHMS'),
        (BPT, 'BPT'),
        (MPT, 'MPT'),
        (BVSc, 'BVSc'),
        (MSc, 'MSc'),
        (DGO, 'DGO'),
        (FRCS, 'FRCS'),
        (MRCP, 'MRCP'),
        (DCH, 'DCH'),
        (DPH, 'DPH'),
        (DDS, 'DDS'),

    ]
    degree = models.CharField(max_length=50, choices=DEGREE_CHOICES,null=True)
    speciality = models.CharField(max_length=100,null=True)


class Disease(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Name of the disease
    # Whether the disease is considered special/private
    is_special = models.BooleanField(default=False)
    # description = models.TextField(blank=True, null=True)  # Optional description of the disease
    # symptoms = models.TextField(blank=True, null=True)  # Optional symptoms related to the disease
    # category = models.CharField(max_length=255, blank=True, null=True)  # Optional category for classification

    def __str__(self):
        return self.name
