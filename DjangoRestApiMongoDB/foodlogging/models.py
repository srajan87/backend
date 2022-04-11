from datetime import datetime
from django.db import models
from django.forms import TimeField
#from django.forms import TimeField
from mongoengine import *
import datetime

# Create your models here.

class FoodLogs(Document):
    log_id = IntField()
    user_id = StringField(max_length=80)
    food_id = StringField()
    meal_tstamp = DateTimeField()
    meal_category = ListField(StringField(max_length=80))
    serving_measurement = DictField()
    nutrition_facts = DictField()
    log_tstamp = DateTimeField(default=datetime.datetime.now)