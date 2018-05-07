from django.db import models
from django.core.urlresolvers import reverse
import datetime

# Create your models here.

class Stats(models.Model):


    property_name = models.CharField(max_length=50)
    property_address1 = models.CharField(max_length=50)
    property_address2 = models.CharField(max_length=20)
    property_address3 = models.CharField(max_length=10)
    property_address4 = models.CharField(max_length=10)
    unit_name = models.CharField(max_length=260)
    tenant_name = models.CharField(max_length=150)
    lease_start = models.CharField(max_length=25)
    lease_end = models.CharField(max_length=25)
    #lease_start = models.DateField(input_formats = settings.DATE_INPUT_FORMATS)
    #lease_end = models.CharField(input_formats = settings.DATE_INPUT_FORMATS)
    lease_years = models.IntegerField()
    current_rent = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.tenant_name

    class Meta:
        ordering = ['current_rent']


    def get_absolute_url(self):
        return reverse("mobile:list")


