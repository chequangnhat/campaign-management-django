# Generated by Django 4.1.5 on 2023-01-05 07:27

from django.db import migrations, models
import django.db.models.deletion
from datetime import datetime

def insert_user(apps, scheme_editor):
  User = apps.get_model('campaignapp', 'User')
  user1 = User(email = "nhat@gmail.com", password = "nhatnhat", first_name = "Quang", last_name = "Nhat", phone_number = "0934676767")
  user1.save()

def insert_data(apps, scheme_editor):
  pass

class Migration(migrations.Migration):

  initial = True

  dependencies = [
    ('campaignapp', '0001_initial')
  ]

  operations = [
    migrations.RunPython(insert_user, reverse_code=insert_data),
  ]
