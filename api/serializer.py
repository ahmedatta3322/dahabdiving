from rest_framework import serializers
from divers.models import Divers
class DiverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Divers
        fields = ['name', 'age'] 
    def validate_name(self , value):
        q = Divers.objects.filter(name__iexact = value)
        if q.exists():
            raise serializers.ValidationError("name wrong")
        return value
