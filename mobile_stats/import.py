import csv, sys, os

project_dir = "/Users/femi/PycharmProjects/Bink/mobile_stats/mobile_stats"

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django
django.setup()
from mobile.models import Stats
data = csv.reader(open("/Users/femi/PycharmProjects/Bink/mobile_stats/Mobile_Phone_Masts.csv"), delimiter=",")

for row in data:
    #importing each record into the database
    if row[0] != 'Property Name':
        stats = Stats()
        stats.property_name = row[0]
        stats.property_address1 = row[1]
        stats.property_address2 = row[2]
        stats.property_address3 = row[3]
        stats.property_address4 = row[4]
        stats.unit_name = row[5]
        stats.tenant_name = row[6]
        stats.lease_start = row[7]
        stats.lease_end = row[8]
        stats.lease_years = row[9]
        stats.current_rent = row[10]
        stats.save()
