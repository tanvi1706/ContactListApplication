from django.db import models

# Create your models here.
class contact(models.Model):
    contact_id = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=25)
    mname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)

class address(models.Model):
    address_id = models.IntegerField(primary_key=True)
    contact_id = models.ForeignKey(contact, on_delete=models.CASCADE)
    address_type = models.CharField(max_length=20)
    address = models.CharField(max_length=35)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=15)
    zip = models.CharField(max_length=5)

class phone(models.Model):
    phone_id = models.IntegerField(primary_key=True)
    contact_id = models.ForeignKey(contact, on_delete=models.CASCADE)
    phone_type = models.CharField(max_length=15)
    area_code = models.CharField(max_length=3)
    number = models.CharField(max_length=12)

class date(models.Model):
    d_id = models.IntegerField(primary_key=True)
    contact_id = models.ForeignKey(contact, on_delete=models.CASCADE)
    date_type = models.CharField(max_length=20)
    d_date = models.DateField()


