from rest_framework import serializers
from .models import TrafficLight


class TrafficLightSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrafficLight #what model you want to serializers
        #fields = ('username') #all the information that you want to make available to the users of the API
        fields = '__all__' #do this to return everything