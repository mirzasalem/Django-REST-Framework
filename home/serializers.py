from rest_framework import serializers
from .models import Person , Country

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class CountrySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Country
        fields = ['country_name', 'id']


class PeopleSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    country_info = serializers.SerializerMethodField()
    
    class Meta:
        model = Person
        # exclude = ['name', 'age']
        fields = '__all__'
        depth = 1 #To find country name
    # def get_country_info(self, c_i):
    #     country_c_i = country_c_i.objects.get(id = c_i.country.id)
    # return {'country_name': country_c_i.country_name, 'he'}
        
    #For validation
    def validate(self, data):
        
        if data ['age'] < 18:
            raise serializers.ValidationError('age should be greater than 18')
        

        spectial = "!@#$%^&*()_+"
        if any(c in spectial for c in data['name']):
            raise serializers.ValidationError('Name cannot contain Special char')
        
        return data
