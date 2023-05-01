from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator

# Create your models here.
class User(AbstractUser):
    pass

# Median Household Income Model
class MedianHouseholdIncome(models.Model):
    """Model representing median household income data"""
    geoid = models.CharField(max_length=7)
    name = models.TextField()
    median_hh_income = models.IntegerField()
    moe = models.IntegerField()
    year = models.IntegerField()
    geography_name = models.CharField(max_length=10)
    state_name = models.CharField(max_length=25)
    state_fips = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    state_abb = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    geography_code = models.CharField(max_length=2, validators=[MinLengthValidator(2)])

    def __str__(self):
        return self.name





