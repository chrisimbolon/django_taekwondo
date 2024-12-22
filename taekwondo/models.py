from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User
from django_countries.fields import CountryField



class Province(models.Model):  # Province/State
    province_name = models.CharField(max_length=150)
    country = CountryField()

    def __str__(self):
        return f"{self.province_name}, {self.country}"

class City(models.Model):  # City
    city_name = models.CharField(max_length=200)
    province = models.ForeignKey('Province', on_delete=models.CASCADE, related_name='cities', null=True, blank=True)

    def __str__(self):
        if self.province:
            return f"{self.city_name}, {self.province.province_name}, {self.province.country}"
        return f"{self.city_name} (No Province)"

    def testing_function(self):
        return self.province

class Belt(models.Model):
    rank_name = models.CharField(max_length=50)
    rank_level = models.PositiveIntegerField()  # Level (e.g., 1 for White, 2 for Yellow)
    is_black_belt = models.BooleanField(default=False)

    def __str__(self):
        return self.rank_name

class Coach(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    registration_number = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=50)
    place_of_birth = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    dojang_name = models.CharField(max_length=30)
    sex = models.CharField(max_length=15,choices=(
        ('male','Male'),
        ('female','Female')
    ))
    province = models.ForeignKey('Province', on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True)
    status =models.CharField(max_length=15,choices=(
        ('active','Active'),
        ('inactive','Inactive')
    ))
    belt = models.ForeignKey('Belt', on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    photo = models.ImageField(upload_to='images/',blank=True)
    input_date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['-id']

