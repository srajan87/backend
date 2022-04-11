from rest_framework_mongoengine import serializers 
from foodlogging.models import FoodLogs
 
 
class FoodLogsSerializer(serializers.DocumentSerializer):
 
    class Meta:
        model = FoodLogs
        fields = (
                  'log_id',
                  'user_id',
                  'food_id',
                  'meal_tstamp',
                  'meal_category',
                  'serving_measurement',
                  'nutrition_facts',
                  'log_tstamp')